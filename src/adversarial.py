"""
TODO
"""

import torch
import torch.nn.functional as F


def fgsm_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Fast Gradient Sign Method Attack, no target class
    """

    model.eval()
    image.grad = None

    if not image.requires_grad:
        image.requires_grad = True

    output = model(image)
    F.nll_loss(output, label).backward()

    return image + epsilon * image.grad.data.sign()


def tfgsm_attack(model: torch.nn.Module, image: torch.tensor, target: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Fast Gradient Sign Method Attack, with target class
    """

    model.eval()

    image.grad = None
    image.requires_grad = True

    output = model(image)
    F.nll_loss(output, target).backward()

    return image - epsilon * image.grad.data.sign()


def bim_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, alpha: float, stop_threshold=0.01, **kwargs) -> torch.tensor:
    """
    Basic Iterative Method Attack, no target class
    (Also known as IFGSM)
    """

    model.eval()
    image.grad = None
    atk_image = image.clone().detach()

    if not atk_image.requires_grad:
        atk_image.requires_grad = True

    for _ in range(kwargs.get("num_iter", 10)):
        F.nll_loss(model.forward(atk_image), label).backward()

        conf = F.softmax(model(atk_image))[0][label]

        if conf.item() < stop_threshold:
            break

        atk_image.data = image + torch.clamp((atk_image.data + (alpha * atk_image.grad.data.sign())) - image, -epsilon, epsilon)


    return atk_image


def tbim_attack(model: torch.nn.Module, image: torch.tensor, target: torch.tensor, epsilon: float, alpha=0.005, stop_threshold=0.5, exit_when_predicted=True, **kwargs) -> torch.tensor:
    """
    Basic Iterative Method Attack, with target class
    """

    model.eval()
    image.grad = None
    atk_image = image.clone().detach()

    if not atk_image.requires_grad:
        atk_image.requires_grad = True

    for _ in range(kwargs.get("num_iter", 10)):
        output = model.forward(atk_image)

        conf = F.softmax(model(atk_image), dim=1)[0][target]

        if conf >= stop_threshold or (exit_when_predicted == True and torch.argmax(model(atk_image), dim=1) == target):
            break

        F.nll_loss(output, target).backward()

        atk_image.data = image + torch.clamp((atk_image.data - (alpha * atk_image.grad.data.sign())) - image, -epsilon, epsilon)

    return atk_image


def cw_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Carlini & Wagner Attack, no target class
    """

    pass


def df_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Deepfool Attack, no target class
    """

    pass


def lbfgs_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Limited-memory Broyden-Fletcher-Goldfarb-Shanno (L-BFGS) Attack, no target class
    """

    pass


def jsma_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Jacobian-based Saliency Map Attack (JSMA) Attack, no target class
    """

    pass


def pgd_attack(model: torch.nn.Module, image: torch.tensor, label: torch.tensor, epsilon: float, **kwargs) -> torch.tensor:
    """
    Projected Gradient Descent Attack, no target class
    """

    pass


def select_attack(name: str) -> lambda **kwargs: torch.tensor:
    return {
        "fgsm": fgsm_attack,
        "tfgsm": tfgsm_attack,
        "bim": bim_attack,
        "tbim": tbim_attack,
        "cw": cw_attack,
        "df": df_attack,
    }.get(name, lambda **kwargs: None)