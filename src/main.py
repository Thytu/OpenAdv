import json
import torch
import adversarial
import data_handler
import gradio as gr


CLS_IDX = json.load(open('./data/imagenet_1k_cls_idx.json'))
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def play_attack(img, attack_name, epsilon, alpha, num_iter, target=None):
    """
    imask, timask, fgsm, tfgsm, bim, tbim
    """

    if target is not None:
        target = torch.tensor(int(list(CLS_IDX.keys())[list(CLS_IDX.values()).index(target)])).unsqueeze(0).to(DEVICE)

    original_image = data_handler.np_array_to_tensor_image(img, device=DEVICE)
    normalized_image = data_handler.normalize_tensor(original_image)

    model_predictions = torch.softmax(model(normalized_image), dim=1)
    label = torch.argmax(model_predictions, dim=1)
    labels = {CLS_IDX[str(idx)]: confidence for idx, confidence in enumerate(model_predictions.detach().cpu().tolist()[0])}

    perturbed_data = adversarial.select_attack(attack_name)(model, normalized_image, label=label, epsilon=epsilon, alpha=alpha, num_iter=num_iter, target=target)

    model_predictions_w_attack = torch.softmax(model(perturbed_data), dim=1)
    labels_w_attack = {CLS_IDX[str(idx)]: confidence for idx, confidence in enumerate(model_predictions_w_attack.detach().cpu().tolist()[0])}

    perturbed_data = torch.clamp(data_handler.unnormalize_tensor(perturbed_data), 0, 1)

    return data_handler.tensor_to_image(original_image), labels, data_handler.tensor_to_image(perturbed_data), labels_w_attack


if __name__ == '__main__':

    model = torch.hub.load('pytorch/vision:v0.10.0', 'vgg19', pretrained=True)
    # model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
    best_test_acc = None

    iface = gr.Interface(fn=play_attack, inputs=[
        gr.inputs.Image(label="Image to feed"),
        gr.inputs.Radio(["fgsm", "tfgsm", "bim", "tbim"]),
        gr.inputs.Number(default=0.005, label="epsilon"),
        gr.inputs.Number(default=0.002, label="alpha"),
        gr.inputs.Slider(minimum=1, maximum=100, step=1, default=10, label="iterations"),
        gr.inputs.Dropdown(list(CLS_IDX.values()), label="Target class")
    ], outputs=[
        gr.outputs.Image(label="Image fed to model"),
        gr.outputs.Label(num_top_classes=3, label="Predicted label"),
        gr.outputs.Image(label="Image after attack"),
        gr.outputs.Label(num_top_classes=3, label="Predicted label after attack"),
    ],
        layout="horizontal", title="OpenAdv",
        description="Userfriendly adversarial attack tool to demonstrate the effectiveness of different attacks on a model, here VGG19. For more information, please read the article below.",
        article=open("article.html", "r").read(), theme="huggingface",
    )

    # params = open("params.md", "r").read()
    # print(params)

    iface.launch(enable_queue=False)
