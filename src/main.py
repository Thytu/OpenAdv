import torch
import matplotlib.pyplot as plt
from torchvision.models import vgg19

import adversarial
import data_handler

# TODO: create a web interface to play with the parameters + describe how does the used attack works + let the user choose attack & image

def play_attack(name, model, image, **kwargs):
    print('\033[1m' + name + '\033[0m')

    perturbed_data = adversarial.select_attack(name)(model, image, **kwargs)

    f = plt.figure()

    f.add_subplot(1, 2, 1)
    plt.title("Image")
    plt.imshow(data_handler.tensor_to_image(image))

    f.add_subplot(1, 2, 2)
    plt.title(f"{name} e:{kwargs['epsilon'] if 'epsilon' in kwargs else '_'} a:{kwargs['alpha'] if 'alpha' in kwargs else '_'}")
    plt.imshow(data_handler.tensor_to_image(perturbed_data))

    plt.show()

    print(f"Expected: {label} and got {torch.argmax(model(image), dim=1)}")
    print(f"Expected: {label} and got {torch.argmax(model(perturbed_data), dim=1)}")


if __name__ == '__main__':

    ACOUSTIC_GUITAR = 402
    WELSH_SPRINGER_SPANIEL = 218
    DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model = vgg19(pretrained=True).eval().to(device=DEVICE)

    best_test_acc = None

    image = data_handler.load_image_to_tensor("./data/images/acoustic guitar.jpeg", device=DEVICE)
    label = torch.LongTensor([ACOUSTIC_GUITAR]).to(DEVICE)
    target = torch.LongTensor([WELSH_SPRINGER_SPANIEL]).to(DEVICE)

    # play_attack("imask", model, image, label=label, epsilon=0.005)
    # play_attack("timask", model, image, label=label, target=target, epsilon=0.005)
    # play_attack("fgsm", model, image, label=label, epsilon=0.005)
    # play_attack("tfgsm", model, image, target=target, epsilon=0.005)
    # play_attack("bim", model, image, label=label, epsilon=0.005, alpha=0.005)
    # play_attack("tbim", model, image, target=target, epsilon=0.01, alpha=0.025)