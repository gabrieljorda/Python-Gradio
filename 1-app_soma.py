import gradio as gr 

def somar(a, b):
    return a + b

print(somar(5,2))

iface = gr.Interface(
    fn=somar ,
    inputs = ["number", "number"],
    outputs = "number",
    title = "calculadora de soma",
    description="insira dois numeros para somar",
    theme = "default"
)

iface.launch() # para rodar o codigo