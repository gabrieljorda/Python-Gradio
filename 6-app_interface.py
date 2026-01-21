import gradio as gr

def customizar_texto(texto,cor_fundo,cor_texto,tamanho_fonte,estilo_fonte):
    estilo = (
        f"color:{cor_texto};"
        f"background-color:{cor_fundo};"
        f"font-size:{tamanho_fonte};"
        f"font-style:{estilo_fonte};"
    )
    return f"<div style='{estilo}'>{texto}</div>"


iface = gr.Interface(
    fn = customizar_texto,
    inputs = [
        gr.Textbox(label="Texto" , placeholder="Digite o texto aqui..."),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho da Fonte", step=1),
        gr.Radio(
            choices = ["normal", "italic", "oblique"],
            label="Estilo da Fonte",
        )
    ],
    outputs = gr.HTML(label="Texto Customizado"),
    title = "Customizador de Texto",
    description = "Esse app permite customizar o texto de acordo com as suas preferências."
)
    
iface.launch()
