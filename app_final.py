import gradio as gr
import string
from collections import Counter

def converter_temperatura(temperatura, escala):
    if escala == "celcius":
        return (temperatura * 9.0/5.0) + 32
    else:
        return (temperatura - 32) * 5.0/9.0

def analizar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_limpo.lower().split()
    num_palavras = len(texto)
    num_caracteres = len(palavras)
    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    
    return num_caracteres, num_palavras, frequencia_html


def criar_relatorio(temperatura, escala,condicao,texto):
    temperatura_convertida = converter_temperatura(temperatura, escala)
    num_palavras, num_caracteres, frequencia = analizar_texto(texto)

    relatorio = (
        f"**Relatório de Clima**\n\n"
        f'Temperatura: {temperatura_convertida:.2f}{"F" if escala == "Celcius" else "C"}\n\n'
        f"Condição: {condicao}\n"
        f"Descrição:{texto}\n\n"
        f"Número de Palavras: {num_palavras}\n"
        f"Número de Caracteres: {num_caracteres}\n"
        f"Frequência de Palavras:\n{frequencia}"
    )
    
    return relatorio

iface = gr.Interface(
    fn=criar_relatorio,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(choices=["Celcius", "Fahrenheit"], label="Converter de"),
        gr.Dropdown(choices=["Ensolarado", "Chuvoso", "Nublado","frio","quente"], label="Condição do Clima"),
        gr.Textbox(label="Descrição do Clima", placeholder="Digite a descrição aqui...", lines=6)
    ],
    outputs=gr.Textbox(label="Relatório de Clima", lines=20),
    title="Gerador de Relatório de Clima",
    description="Esse app gera um relatório de clima baseado na temperatura, condição e descrição fornecidas."
)

iface.launch()
