import gradio as gr
import numpy as np
from PIL import Image
import io
import base64


def criar_slide(titulo , texto , imagem , cor_fundo , cor_texto):
    estilo = (
        f"background-color:{cor_fundo};"
        f"color:{cor_texto};"
        "padding:20px;"
        "text-align:center;"
    )
    #coverter a imagem para base64
    imagem_html = ""
    if imagem is not None:
        buffered = io.BytesIO()
        imagem.formarray(imagem).save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        imagem_html = f"<img src='data:image/png;base64,{img_str}' alt='Imagem do Slide' style='max-width:100%; height:auto;'/>"

    slide_html = f"""
    <div style='{estilo}'>
        <h1>{titulo}</h1>
        <p>{texto}</p>
        {imagem_html}
    </div>
    """
    return slide_html

iface = gr.Interface(
    fn = criar_slide,
    inputs=[
        gr.Textbox(label="Título do Slide", placeholder="Digite o título aqui..."),
        gr.Textbox(label="Texto do Slide", placeholder="Digite o texto aqui..."),
        gr.Image(label="Imagem do Slide", type="numpy"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
    ],
    outputs=gr.HTML(label="Slide customizado"),
    title="Criador de Slides Customizados",
    description="Esse app permite criar slides customizados com título, texto, imagem e cores de fundo e texto."
)

iface.launch()