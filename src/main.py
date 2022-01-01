import json
import torch
import adversarial
import data_handler
import gradio as gr


def play_attack(img, attack_name, epsilon, alpha, num_iter):
    """
    imask, timask, fgsm, tfgsm, bim, tbim
    """

    image = data_handler.np_array_to_tensor_image(img, device=DEVICE)

    model_predictions = torch.softmax(model(image), dim=1)
    label = torch.argmax(model_predictions, dim=1)
    labels = {CLS_IDX[str(idx)]: confidence for idx, confidence in enumerate(model_predictions.detach().cpu().tolist()[0])}

    perturbed_data = adversarial.select_attack(attack_name)(model, image, label=label, epsilon=epsilon, alpha=alpha, num_iter=num_iter, target=None)

    model_predictions_w_attack = torch.softmax(model(perturbed_data), dim=1).detach().cpu().tolist()[0]
    labels_w_attack = {CLS_IDX[str(idx)]: confidence for idx, confidence in enumerate(model_predictions_w_attack)}

    return data_handler.tensor_to_image(image), labels, data_handler.tensor_to_image(perturbed_data), labels_w_attack


if __name__ == '__main__':

    CLS_IDX = json.load(open('./data/imagenet_1k_cls_idx.json'))
    DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
    best_test_acc = None

    iface = gr.Interface(fn=play_attack, inputs=[
        gr.inputs.Image(label="Image to feed"),
        gr.inputs.Radio(["imask", "timask", "fgsm", "tfgsm", "bim", "tbim"]),
        gr.inputs.Number(default=0.005, label="epsilon"),
        gr.inputs.Number(default=0.002, label="alpha"),
        gr.inputs.Slider(minimum=1, maximum=100, step=1, default=10, label="iterations"),
    ], outputs=[
        gr.outputs.Image(label="Image fed to model"),
        gr.outputs.Label(num_top_classes=3, label="Predicted label"),
        gr.outputs.Image(label="Image after attack"),
        gr.outputs.Label(num_top_classes=3, label="Predicted label after attack"),
    ],
        layout="horizontal", title="Play Attack", description="""
        Demo of different types of adversarial attack

        IMask: Attack the model by perturbing the input image
        Usage: imask <image> <epsilon> <iterations>

        TIMask: Attack the model by perturbing the input image
        Usage: imask <image> <epsilon> <target> <iterations>

        FGSM: Attack the model by perturbing the input image
        Usage: fgsm <image> <epsilon>

        TFGSM: Attack the model by perturbing the input image
        Usage: tfgsm <image> <epsilon> <target>

        BIM: Attack the model by perturbing the input image
        Usage: bim <image> <epsilon> <alpha> <iterations>

        TBIM: Attack the model by perturbing the input image
        Usage: tbim <image> <epsilon> <alpha> <target> <iterations>
        """, theme="huggingface"
    )

    iface.launch()
