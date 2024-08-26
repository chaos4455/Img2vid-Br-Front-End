# 🎨 **Img2vid-Br-Front-End** 🎨

🚀 **Transforme Imagens em Vídeos com Facilidade!** 🎥

🔍 **Explore o Poder da IA Generativa - Apenas execute o script e ele fará todo o download dos modelos localmente. Antes disso instale o python versão 3.10 ou superior e as dependencias ** 🤖

# 🚀 Projeto Img2vid-Br-Front-End

Este projeto utiliza o modelo `Img2Vid` da Stability AI para transformar imagens estáticas em vídeos dinâmicos. Abaixo estão alguns exemplos de vídeos gerados com o modelo, demonstrando suas capacidades de animação e transformação.


### 📦 Dependências e Instalação:

Certifique-se de ter o **Python** instalado. Em seguida, instale as bibliotecas necessárias com o comando:

```bash
pip install torch diffusers gradio pillow
```


# 🚀 Criei esse repositório pra mostrar meus conhecimentos e habilidades em trabalhar com interfaces e back ends de IA generativa de última geração utilizando abordagem simples e funcional para implementações peformáticas e de simples implentação no estado da arte.

Se você está interessado em **IA generativa** e quer explorar mais, **não hesite em me contatar** no meu linkedin🌟

**Vamos juntos descobrir ainda mais aplicações pra tecnologias de IA generativa!** 💪🎥✨

Maringá 26 08 2024 - Elias Andrade


Lógica detalhada usada no desenvolvimento do projeto:

- 📂 **Projeto: Gerador de Vídeo com Stable Video Diffusion**
  - 🔄 **Tecnologia e Bibliotecas**
    - 🛠️ **Python**
    - 🔧 **Bibliotecas:**
      - 📦 **torch** (PyTorch)
      - 🖼️ **PIL** (Pillow)
      - 🧩 **diffusers** (Stable Video Diffusion)
      - 🌐 **gradio** (Interface Gráfica)
      - 📅 **datetime** (Data e Hora)
      - 🆔 **uuid** (Identificadores Únicos)
      - 🗂️ **os** (Sistema de Arquivos)

  - 🧩 **Funções**
    - 📏 **resize_image(image, size_option)**
      - 🔍 **Obter tamanho original da imagem**
      - 🔢 **Verificar tipo de `size_option`**
        - 🧮 **Tamanho fixo**: Redimensionar para `size_option`
        - 📉 **Porcentagem**: Calcular novo tamanho com base na porcentagem
      - 🔄 **Redimensionar imagem** com antialiasing (Image.LANCZOS)

    - 🎬 **generate_video(image_path, num_frames, fps, decode_chunk_size, motion_bucket_id, noise_aug_strength, seed, size_option)**
      - 🧪 **Verificar validade do caminho da imagem**
        - ❌ **Caminho inválido**: Retornar erro
      - 🔧 **Configuração do Pipeline**
        - 📦 **Carregar modelo** (StableVideoDiffusionPipeline)
        - ⚙️ **Configurar descarregamento de modelo para CPU**
      - 📷 **Carregar e Redimensionar Imagem**
        - 🖼️ **Carregar imagem** (load_image)
        - 📏 **Redimensionar imagem** (resize_image)
      - 🔢 **Definir gerador e semente** (torch.manual_seed)
      - 🎞️ **Gerar Frames**
        - 🔄 **Loop para geração em chunks**
        - 📈 **Adicionar frames gerados** ao array
      - 📁 **Gerar Nome Único para Arquivo**
        - 📅 **Data e Hora** + 🆔 **UUID**
      - 💾 **Exportar Vídeo** (export_to_video)
      - ✅ **Retornar Nome do Arquivo e Mensagem de Sucesso**

  - 🖥️ **Interface Gradio**
    - 🧩 **Blocos de Interface**
      - 🏷️ **Markdown**
        - 📝 **Título e Instruções**
        - 🖼️ **Prévia da Imagem**
        - 📋 **Informações sobre salvamento do vídeo**
        - 🌟 **Mensagens encorajadoras**
      - 📥 **Inputs**
        - 📁 **Imagem de Entrada** (gr.Image)
        - 📏 **Tamanho da Imagem/Vídeo** (gr.Dropdown)
        - 🎞️ **Número de Frames** (gr.Slider)
        - ⏱️ **FPS** (gr.Slider)
        - 🧩 **Tamanho do Chunk** (gr.Slider)
        - 🎯 **ID do Bucket de Movimento** (gr.Slider)
        - 🔊 **Intensidade de Aumento de Ruído** (gr.Slider)
        - 🌱 **Seed para Geração Aleatória** (gr.Number)
      - 🚀 **Botão de Geração** (gr.Button)
        - 🔄 **Chamar Função `generate_video`**
      - 📽️ **Saídas**
        - 🎥 **Vídeo Gerado** (gr.Video)
        - 📝 **Mensagem de Status** (gr.Textbox)

  - 🚀 **Execução**
    - 🎯 **Lançar Interface Gradio** (demo.launch())

# 🌐 Portfólio & Contato

Sou um especialista em **IA generativa avançada** e sempre busco novos desafios e oportunidades de aprendizado. Você pode conferir mais sobre meu trabalho e projetos em andamento nos links abaixo:

- **LinkedIn**: [Elias Andrade](https://www.linkedin.com/in/itilmgf/)
- **GitHub**: [Meu Repositório](https://github.com/chaos4455/)

---

https://github.com/user-attachments/assets/a5bfc5ec-a5d0-4ba1-ac9a-b2c01a39ce82



https://github.com/user-attachments/assets/a2cecd97-af43-4864-b233-a79e27344d36



https://github.com/user-attachments/assets/6dd07ced-b90a-4719-819d-de38a118c7c6



Após instalação acesse o endereço do web app localmente via http://127.0.0.1:7860

---

🌟 **Projeto**: Img2vid-Br-Front-End  
🔧 **Tecnologia**: Gradio, Stable Video Diffusion  
🎯 **Objetivo**: Fornecer uma interface intuitiva para gerar vídeos a partir de imagens  
🌐 **Inspiração**: Comunidade Hugging Face  
💻 **Hardware**: Testado em RTX 2060 de 12GB  


**Bem-vindo ao meu projeto Img2vid-Br-Front-End!** Aqui, eu desenvolvi uma interface **front-end** intuitiva e poderosa utilizando **Gradio** para facilitar o uso e os testes com o modelo **Img2Vid** da **Stability AI**. Meu objetivo foi criar uma ferramenta acessível para gerar vídeos a partir de imagens, aproveitando o potencial de IA generativa avançada. 🚀

## 🚀 Exemplo de Imagem Estática de Foguete 

## 🖼️ Exemplo de Capacidade do Modelo Stability-AI Img2Vid (Fonte: Stability AI)

![Capacidade do Modelo Stability-AI Img2Vid](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/output_tile.gif?raw=true))

*Esta imagem é um exemplo do que o modelo Stable Video Diffusion da Stability AI pode fazer, transformando uma imagem estática em uma animação fluida.* 

![Exemplo de Foguete Estático](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/rocket.png?raw=true)

*Uma imagem simples de um foguete antes da animação. Esta imagem estática foi utilizada como entrada para o modelo.*


## 🎞️ Resultado da Animação do Foguete (Fonte: Stability AI)

![Resultado da Animação do Foguete](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/output_rocket_with_conditions.gif?raw=true)

*Resultado da animação gerada a partir da imagem estática do foguete. Este exemplo foi baseado no paper oficial da Stability AI.*


## 🖥️ Print da Minha Interface

![Minha Interface](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/chrome_qB6sC8rtiG.png?raw=true)

*Aqui está a interface do meu projeto, que foi desenvolvida para facilitar o uso e a experimentação com o modelo img2vid.*



## 📊 Gráfico de Consumo de Hardware no Meu PC

![Gráfico de Consumo de Hardware](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/Taskmgr_3CMUvRFKUC.png?raw=true)

*Gráfico de monitoramento de recursos no meu PC durante a execução do modelo img2vid. Como você pode ver, o consumo de GPU e CPU é significativo, especialmente para placas abaixo de uma 4090.*

---

## 💡 Visão Geral do Projeto

Este projeto foi inspirado por vários exemplos impressionantes da comunidade **Hugging Face**, como:
- **[Stable Video Diffusion Upscale](https://huggingface.co/spaces/asahi417/stable-video-diffusion-upscale)**: uma abordagem incrível para a criação de vídeos de alta qualidade usando difusão.
- **[AnimateLCM-SVD](https://huggingface.co/spaces/wangfuyun/AnimateLCM-SVD)**: uma aplicação inovadora que anima imagens com detalhes realistas.
- 
## 🖥️ Exemplo da Interface do Repositório de Inspiração 1

![Interface do Repositório de Inspiração 1](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/chrome_thPz0v6TcW.png?raw=true)

*Este print mostra a interface de um dos repositórios que me serviu de inspiração para este projeto.*

## 🖥️ Print do Projeto 2 que Me Inspirou

![Projeto de Inspiração 2](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/chrome_bV3oUJhC5J.png?raw=true)

*Este é um print de outro projeto que me inspirou na criação deste front-end.*


Com esses exemplos em mente, decidi construir minha própria versão que oferece uma experiência simplificada para usuários que desejam explorar as capacidades dos modelos de difusão. 😎

---

## 🖼️ Características do Projeto

Este projeto permite que você:

- **Carregue uma imagem** e a processe com facilidade.
- **Ajuste parâmetros avançados** como número de frames, FPS, tamanho do chunk de decodificação, e intensidade de ruído para gerar vídeos personalizados. 🎛️
- **Visualize uma prévia** da imagem selecionada e do vídeo gerado diretamente na interface.
- **Salve automaticamente** o vídeo gerado na raiz do projeto. 💾

### Modelos Compatíveis:
- **[stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt)**: Recomendado para placas de vídeo como **RTX 4090** ou GPUs de alto desempenho. ⚙️
- **[stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid)**: Ideal para placas de vídeo como **RTX 3060** ou inferiores. 💻

---

## ⚙️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto. 🐍
- **Gradio**: Utilizado para criar a interface front-end interativa. 🌐
- **Stable Video Diffusion Pipeline**: Modelo de IA que realiza a difusão para criação de vídeos. 🎞️
- **PIL (Python Imaging Library)**: Para manipulação e redimensionamento de imagens. 🖼️
- **Torch**: Biblioteca usada para a manipulação de tensores e execução de cálculos em GPUs. 🚀



# 🎯 Objetivo do Projeto

Este projeto não é apenas uma ferramenta, mas um **exemplo prático** de como a **IA generativa** pode ser utilizada para transformar **imagens estáticas** em **vídeos dinâmicos**. Ele foi projetado para **entusiastas** e **profissionais** que desejam explorar as possibilidades de IA generativa **sem complicações técnicas**.

Desenvolver este **front-end** foi um desafio interessante e gratificante, e espero que você aproveite tanto quanto eu ao usá-lo! 🎉

---



