import gradio as gd
from sympy import true
from transformers import pipeline
from PIL import Image


def remove_background(img_path):
    pipeline_model = pipeline(
        "image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True
    )
    pipeline_model(img_path, return_mask=True)
    image_pillow = pipeline_model(img_path)
    return image_pillow


remove_background("img/img1.jpg")

app = gd.Interface(
    title="Remove o Fundo da Imagem",
    description="Faça upload da imagem para remover o fundo",
    fn=remove_background,
    inputs=gd.components.Image(type="pil"),
    outputs=gd.components.Image(type="pil", format="png"),
)

if __name__ == "__main__":
    app.launch(share=true)
