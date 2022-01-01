import torch
import torchvision.transforms as transforms

from PIL import Image


IMG_SIZE = 512 if torch.cuda.is_available() else 128
COMPOSED_TRANSFORMERS = transforms.Compose([
    transforms.Resize(IMG_SIZE),
    transforms.ToTensor(),
])


def load_image_to_tensor(image_name, width=IMG_SIZE, height=IMG_SIZE, device='cpu') -> torch.tensor:
    image = Image.open(image_name).convert('RGB').resize((width, height))
    image = COMPOSED_TRANSFORMERS(image).unsqueeze(0)

    return image.to(device, torch.float)


def np_array_to_tensor_image(img, width=IMG_SIZE, height=IMG_SIZE, device='cpu'):
    image = Image.fromarray(img).convert('RGB').resize((width, height))
    image = COMPOSED_TRANSFORMERS(image).unsqueeze(0)

    return image.to(device, torch.float)


def tensor_to_image(tensor: torch.tensor) -> Image:
    return transforms.ToPILImage()(tensor.cpu().clone().squeeze(0))
