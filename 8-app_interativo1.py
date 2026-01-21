import gradio as gr

def converter_temperatura(temperatura, escala):
    if escala == "celcius":
        return (temperatura * 9.0/5.0) + 32
    else:
        return (temperatura - 32) * 5.0/9.0
    
iface = gr.Interface(
    fn = converter_temperatura,
    inputs = [
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(choices=["celcius", "fahrenheit"], label="Converter para")
    ],
    outputs = gr.Number(label="Temperatura Convertida", precision=2),
    title="Conversor de Temperatura",
    description="Esse app converte temperaturas entre Celsius e Fahrenheit."
)
iface.launch()
