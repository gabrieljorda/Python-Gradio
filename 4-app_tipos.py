import gradio as gr
def processar_dados(texto,numero,imagem,lista_texto,cor,opcoes):
    testo_revertido = texto[::-1]
    dobro_numero = numero * 2
    mensagem_imagem = F"Imagem recebida!" if imagem else "Não há imagem."
    
    lista_processada = [[item] for item in lista_texto.splitlines()]if lista_texto else []

    return(
        testo_revertido,
        dobro_numero,
        mensagem_imagem,
        lista_processada,
        f"Cor selecionada: {cor}",
        opcoes
    )
    
iface = gr.Interface(
    fn = processar_dados,
    inputs = [
        gr.Textbox(label="Texto",placeholder="Digite um texto aqui"),
        gr.Slider(label ="Número", minimum=0, maximum=100, value=10),
        gr.Image(label="Imagem",type="pil"),
        gr.Textbox(label="Lista de Texto",placeholder="Item1\nItem2", lines=4),
        gr.ColorPicker(label="Escolha uma cor"),
        gr.CheckboxGroup(
            choices=["Opção 1","Opção 2","Opção 3"],
            label="Selecione opções"
        )
    ],
    outputs=[
        gr.Textbox(label="Texto Revertido"),
        gr.Number(label="Número Dobrado"),
        gr.Textbox(label="Mensagem da Imagem"),
        gr.Dataframe(label="Lista Processada",headers=["Item"]),
        gr.Textbox(label="Cor Selecionada"),
        gr.Textbox(label="Opções Selecionadas")
    ],
    title = "Verificados de Tipos de Entrada e saídas",
    description="Insira um texto um número, uma imagem, uma lista de itens, escolha uma cor e selecione opções para ver como cada tipo de entrada é processado e exibido."
)

iface.launch()