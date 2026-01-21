import gradio as gr
import string
from collections import Counter

def analizar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_limpo.lower().split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    
    return num_caracteres, num_palavras, frequencia_html

iface = gr.Interface(
    fn=analizar_texto,
    inputs=[
        gr.Textbox(label="texto", placeholder="Digite o texto aqui...", lines=6)
    ],
    outputs=[
        gr.Number(label="Número de Caracteres"),
        gr.Number(label="Número de Palavras"),
        gr.HTML(label="Frequência de Palavras")
    ],
    title="Analisador de Texto",
    description="Esse app analisa o texto fornecido e retorna o número de caracteres, número de palavras e a frequência de cada palavra."
)
iface.launch()