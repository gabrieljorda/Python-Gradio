import gradio as gr

def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

print(reverter_texto("Hello, Gradio!"))

iface = gr.Interface(
    fn = reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="reversor de texto ",
    description="insira um texto para reverter e contar os caracteres",
    )

iface.launch()  # para rodar o codigo
