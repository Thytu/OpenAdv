import re
from PIL.Image import NONE
import torch
import torch.optim as optim
import torch.nn.functional as F

from tqdm import tqdm


def _create_empty_mask(tensor: torch.tensor) -> torch.tensor:
    """
    Create a zero_like tensor based on the provided tensor
    """

    return torch.zeros_like(tensor, requires_grad=True)


def imask_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, max_iter=10) -> torch.tensor:
    """
    Iterative Attack, no target class
    """

    model.eval()
    image.grad = None
    mask = _create_empty_mask(image)
    opt = optim.SGD([mask], lr=1e-1)

    pbar = tqdm(range(max_iter))
    for t in pbar:

        pred = model(image + mask)
        loss = - torch.nn.CrossEntropyLoss()(pred, label)

        opt.zero_grad()
        loss.backward()
        opt.step()

        mask.data.clamp_(-epsilon, epsilon)

        pbar.set_description(f"iter: {t}, loss: {loss.item():.2f}")

    return torch.clamp(image + mask, 0, 1)


def timask_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, target: torch.tensor, epsilon: float, epoch=50) -> torch.tensor:
    """
    TODO
    """

    model.eval()
    image.grad = None
    mask = _create_empty_mask(image)
    opt = optim.SGD([mask], lr=1e-2)


    pbar = tqdm(range(epoch))
    for t in pbar:
        opt.zero_grad()

        pred = model(image + mask)
        loss = (
            - F.nll_loss(pred, label)
            + F.nll_loss(pred, target)
        )

        loss.backward()

        opt.step()

        mask.data.clamp_(-epsilon, epsilon)
        pbar.set_description(f"epoch: {t}, loss: {loss.item():.2f}")

    return torch.clamp(image + mask, 0, 1)


def fgsm_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float) -> torch.tensor:
    """
    Fast Gradient Sign Method Attack, no target class
    """

    model.eval()
    image.grad = None

    if not image.requires_grad:
        image.requires_grad = True

    output = model(image)
    F.nll_loss(output, label).backward()

    return torch.clamp(image + epsilon * image.grad.data.sign(), 0, 1)


def tfgsm_attack(model: torch.nn.Module, image: torch.tensor, target: torch.tensor, epsilon: float) -> torch.tensor:
    """
    Fast Gradient Sign Method Attack, with target class
    """

    model.eval()

    image.grad = None
    image.requires_grad = True

    output = model(image)
    F.nll_loss(output, target).backward()

    return torch.clamp(image - epsilon * image.grad.data.sign(), 0, 1)


def bim_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, alpha: float, max_iter=100, stop_threshold=0.01) -> torch.tensor:
    """
    Basic Iterative Method Attack, no target class
    (Also known as IFGSM)
    """

    model.eval()
    image.grad = None
    atk_image = image.clone().detach()

    if not atk_image.requires_grad:
        atk_image.requires_grad = True

    pbar = tqdm(range(max_iter))
    for t in pbar:
        F.nll_loss(model.forward(atk_image), label).backward()

        conf = F.softmax(model(atk_image))[0][label]
        pbar.set_description(f"iter: {t}, conf: {conf.item():.6f}")

        if conf.item() < stop_threshold:
            break

        atk_image.data = image + torch.clamp((atk_image.data + (alpha * atk_image.grad.data.sign())) - image, -epsilon, epsilon)


    return torch.clamp(atk_image, 0, 1)


def tbim_attack(model: torch.nn.Module, image: torch.tensor, target: torch.tensor, epsilon: float, alpha=0.005, max_iter=100, stop_threshold=0.5, exit_when_predicted=True) -> torch.tensor:
    """
    Basic Iterative Method Attack, with target class
    """

    model.eval()
    image.grad = None
    atk_image = image.clone().detach()

    if not atk_image.requires_grad:
        atk_image.requires_grad = True

    pbar = tqdm(range(max_iter))
    for t in pbar:
        output = model.forward(atk_image)

        conf = F.softmax(model(atk_image), dim=1)[0][target]
        pbar.set_description(f"iter: {t}, conf: {conf.item():.6f}")

        if conf >= stop_threshold or (exit_when_predicted == True and torch.argmax(model(atk_image), dim=1) == target):
            break

        F.nll_loss(output, target).backward()

        atk_image.data = image + torch.clamp((atk_image.data - (alpha * atk_image.grad.data.sign())) - image, -epsilon, epsilon)


    return torch.clamp(atk_image, 0, 1)


def cw_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float) -> torch.tensor:
    """
    Carlini & Wagner Attack, no target class
    """

    pass


def df_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float) -> torch.tensor:
    """
    Deepfool Attack, no target class
    """

    pass


def select_attack(name: str) -> lambda **kwargs: torch.tensor:
    return {
        "imask": imask_attack,
        "timask": timask_attack,
        "fgsm": fgsm_attack,
        "tfgsm": tfgsm_attack,
        "bim": bim_attack,
        "tbim": tbim_attack,
        "cw": cw_attack,
        "df": df_attack,
    }.get(name, lambda **kwargs: None)