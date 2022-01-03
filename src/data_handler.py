import torch
import torchvision.transforms as transforms

from PIL import Image


IMG_SIZE = 512 if torch.cuda.is_available() else 224
COMPOSED_TRANSFORMERS = transforms.Compose([
    transforms.Resize(IMG_SIZE),
    transforms.ToTensor(),
])

NORMALIZE_TENSOR = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)

UNNORMALIZE_TENSOR = transforms.Normalize(
    mean=[-0.485 / 0.229, -0.456 / 0.224, -0.406 / 0.225],
    std=[1 / 0.229, 1 / 0.224, 1 / 0.225]
)


def load_image_to_tensor(image_name, width=IMG_SIZE, height=IMG_SIZE, device='cpu') -> torch.tensor:
    image = Image.open(image_name).convert('RGB').resize((width, height))
    image = COMPOSED_TRANSFORMERS(image).unsqueeze(0)

    return image.to(device, torch.float)


def np_array_to_tensor_image(img, width=IMG_SIZE, height=IMG_SIZE, device='cpu'):
    image = Image.fromarray(img).convert('RGB').resize((width, height))
    image = COMPOSED_TRANSFORMERS(image).unsqueeze(0)

    return image.to(device, torch.float)


def normalize_tensor(tensor: torch.tensor) -> torch.tensor:
    return NORMALIZE_TENSOR(tensor)


def unnormalize_tensor(tensor: torch.tensor) -> torch.tensor:
    return UNNORMALIZE_TENSOR(tensor)


def tensor_to_image(tensor: torch.tensor) -> Image:
    return transforms.ToPILImage()(tensor.cpu().clone().squeeze(0))
