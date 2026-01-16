import gradio as gr
import math

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Fatorial não definido para números negativos"
    else:
        return math.factorial(n)

iface = gr.Interface(
    fn = fatorial,
    inputs="number",
    outputs="text",
    title="Calculadora de Fatorial",
    description="Insira um número para calcular seu fatorial",
)

iface.launch()  # para rodar o codigo

    
