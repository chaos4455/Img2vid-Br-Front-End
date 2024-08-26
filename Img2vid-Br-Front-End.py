import os  # Importa o módulo os para interagir com o sistema operacional
import torch  # Importa o PyTorch, uma biblioteca de deep learning para manipulação de tensores
from PIL import Image  # Importa o PIL para manipulação de imagens
from diffusers import StableVideoDiffusionPipeline  # Importa o pipeline de difusão estável de vídeos da Stability AI
from diffusers.utils import load_image, export_to_video  # Importa funções auxiliares para carregar imagens e exportar vídeos
import datetime  # Importa datetime para trabalhar com datas e horas
import uuid  # Importa uuid para gerar identificadores únicos
import gradio as gr  # Importa Gradio para criar a interface gráfica

# Função para redimensionar a imagem mantendo a proporção original
def resize_image(image, size_option):
    original_width, original_height = image.size  # Obtém o tamanho original da imagem

    if isinstance(size_option, int):  # Se o tamanho for um número inteiro (tamanho fixo)
        new_width = new_height = size_option  # Define largura e altura como o valor fixo fornecido
    else:  # Se o tamanho for uma porcentagem
        percentage = int(size_option.replace("%", ""))  # Remove o sinal de % e converte para inteiro
        new_width = int(original_width * (percentage / 100))  # Calcula a nova largura baseada na porcentagem
        new_height = int(original_height * (percentage / 100))  # Calcula a nova altura baseada na porcentagem

    return image.resize((new_width, new_height), Image.LANCZOS)  # Redimensiona a imagem com antialiasing

# Função principal para gerar o vídeo
def generate_video(image_path, num_frames, fps, decode_chunk_size, motion_bucket_id, noise_aug_strength, seed, size_option):
    # Verificar se o caminho da imagem é válido
    if not os.path.isfile(image_path):
        return None, f"🚫 O caminho especificado não é válido: {image_path}"  # Retorna erro se o caminho não for válido

    # Configuração do pipeline de difusão de vídeo
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid", torch_dtype=torch.float16, variant="fp16"
    )
    pipe.enable_model_cpu_offload()  # Descarrega partes do modelo para a CPU quando não estiverem em uso para economizar VRAM

    # Carregar e redimensionar a imagem de condicionamento
    image = load_image(image_path)  # Carrega a imagem usando a função utilitária
    image = resize_image(image, size_option)  # Redimensiona a imagem conforme a opção de tamanho escolhida

    # Definir o gerador e a semente para garantir resultados reprodutíveis
    generator = torch.manual_seed(seed)

    # Gerar os frames do vídeo
    frames = []
    for _ in range(num_frames // decode_chunk_size):  # Loop para gerar os frames em chunks
        chunk_frames = pipe(image, decode_chunk_size=decode_chunk_size, generator=generator, motion_bucket_id=motion_bucket_id, noise_aug_strength=noise_aug_strength).frames[0]
        frames.extend(chunk_frames)  # Adiciona os frames gerados ao array de frames

    # Gerar um nome único para o arquivo de saída
    unique_filename = f"generated_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.mp4"

    # Exportar o vídeo
    export_to_video(frames, unique_filename, fps=fps)  # Exporta os frames gerados para um arquivo de vídeo

    return unique_filename, f"✅ Vídeo gerado e salvo como {unique_filename}"  # Retorna o nome do arquivo e uma mensagem de sucesso

# Interface Gradio
with gr.Blocks() as demo:  # Cria um bloco de interface usando Gradio
    gr.Markdown("# 🎥✨ Gerador de Vídeo com Stable Video Diffusion ✨🎥")  # Título principal da interface
    gr.Markdown("## 🖼️ Configure todos os parâmetros para gerar seu vídeo personalizado 🎛️")  # Subtítulo com instruções

    with gr.Row():  # Organiza os elementos em uma linha
        with gr.Column():  # Primeira coluna para as configurações principais
            gr.Markdown("### 🔧 Configurações de Imagem e Vídeo")  # Seção de configurações de imagem e vídeo

            image_input = gr.Image(type="filepath", label="📁 Escolha uma Imagem para Processar")  # Input para selecionar a imagem
            preview_image = gr.Image(label="🖼️ Prévia da Imagem Selecionada")  # Campo para pré-visualizar a imagem
            image_input.change(lambda image: image, image_input, preview_image)  # Atualiza a prévia da imagem quando uma nova imagem é carregada

            size_option = gr.Dropdown(["800", "1024", "2048", "10%", "20%", "25%", "30%", "40%", "50%", "80%"], 
                                      value="800", label="📏 Tamanho Final da Imagem/Vídeo")  # Dropdown para selecionar o tamanho da imagem/vídeo

            num_frames = gr.Slider(16, 64, value=24, step=8, label="🎞️ Número de Frames")  # Slider para definir o número de frames do vídeo
            fps = gr.Slider(1, 30, value=6, step=1, label="⏱️ FPS (Taxa de Quadros)")  # Slider para definir os FPS do vídeo
            decode_chunk_size = gr.Slider(1, 16, value=8, step=1, label="🧩 Tamanho do Chunk de Decodificação")  # Slider para definir o tamanho do chunk de decodificação
            motion_bucket_id = gr.Slider(0, 200, value=90, step=10, label="🎯 ID do Bucket de Movimento")  # Slider para definir o ID do bucket de movimento
            noise_aug_strength = gr.Slider(0.0, 1.0, value=0.1, step=0.05, label="🔊 Intensidade de Aumento de Ruído")  # Slider para definir a intensidade do aumento de ruído

        with gr.Column():  # Segunda coluna para configurações avançadas
            gr.Markdown("### ⚙️ Configurações Avançadas")  # Seção de configurações avançadas

            seed = gr.Number(value=42, label="🌱 Seed (Semente) para Geração Aleatória")  # Campo para definir a semente de geração aleatória

            generate_button = gr.Button("🚀 Gerar Vídeo")  # Botão para iniciar a geração do vídeo

            output_video = gr.Video(label="📽️ Vídeo Gerado")  # Campo para exibir o vídeo gerado
            output_message = gr.Textbox(label="📋 Mensagem de Status")  # Campo para exibir mensagens de status

            generate_button.click(
                generate_video,
                inputs=[image_input, num_frames, fps, decode_chunk_size, motion_bucket_id, noise_aug_strength, seed, size_option],
                outputs=[output_video, output_message]
            )  # Configura o botão para chamar a função generate_video com as entradas e saídas apropriadas

    gr.Markdown("### 💾 O vídeo gerado será salvo na raiz do projeto.")  # Mensagem informativa sobre o local de salvamento do vídeo
    gr.Markdown("### 🌟 Explore as configurações para criar vídeos únicos e personalizados!")  # Mensagem encorajadora para explorar as configurações

demo.launch()  # Lança a interface Gradio para o usuário
