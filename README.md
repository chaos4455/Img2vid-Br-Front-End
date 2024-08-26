# 🎨 **Img2vid-Br-Front-End** 🎨

🚀 **Transforme Imagens em Vídeos com Facilidade!** 🎥

🔍 **Explore o Poder da IA Generativa** 🤖

---

🌟 **Projeto**: Img2vid-Br-Front-End  
🔧 **Tecnologia**: Gradio, Stable Video Diffusion  
🎯 **Objetivo**: Fornecer uma interface intuitiva para gerar vídeos a partir de imagens  
🌐 **Inspiração**: Comunidade Hugging Face  
💻 **Hardware**: Testado em RTX 2060 de 12GB  


**Bem-vindo ao projeto "Gerador de Vídeo com Stable Video Diffusion"!** Aqui, eu desenvolvi uma interface **front-end** intuitiva e poderosa utilizando **Gradio** para facilitar o uso e os testes com o modelo **Img2Vid** da **Stability AI**. Meu objetivo foi criar uma ferramenta acessível para gerar vídeos a partir de imagens, aproveitando o potencial de IA generativa avançada. 🚀

## 🚀 Exemplo de Imagem Estática de Foguete 

## 🖼️ Exemplo de Capacidade do Modelo Stability-AI Img2Vid

![Capacidade do Modelo Stability-AI Img2Vid](https://github.com/chaos4455/Img2vid-Br-Front-End/blob/main/assets/chrome_qB6sC8rtiG.png?raw=true)

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

### 📦 Dependências e Instalação:

Certifique-se de ter o **Python** instalado. Em seguida, instale as bibliotecas necessárias com o comando:

```bash
pip install torch diffusers gradio pillow
```

## 🎥 Vídeo Gerado com o Resultado no Meu PC

![Vídeo Gerado com o Resultado no Meu PC](https://github.com/chaos4455/Img2vid-Br-Front-End/raw/main/assets/generdated.mp4)

*Este vídeo foi gerado no meu próprio PC utilizando o modelo img2vid da Stability AI. Ele demonstra a capacidade do modelo de transformar imagens estáticas em vídeos dinâmicos.*

## 🎥 Vídeo com Variação nos Frames (Mínimo de 6 Frames)

![Vídeo com Variação nos Frames](https://github.com/chaos4455/Img2vid-Br-Front-End/raw/main/assets/generated_20240826_044207_ddc6fad9d9da4ee8898a241423f164d9.mp4)

*Este vídeo mostra uma variação nos frames, o que proporciona uma fluidez mínima ao vídeo. Recomenda-se o uso de pelo menos 6 frames para garantir uma animação suave.*

## 🎥 Outro Vídeo Gerado no Meu Computador

![Outro Vídeo Gerado no Meu Computador](https://github.com/chaos4455/Img2vid-Br-Front-End/raw/main/assets/generated01.mp4)

*Mais um exemplo de vídeo gerado utilizando a ferramenta, demonstrando a capacidade do modelo em produzir diferentes animações a partir de entradas variadas.*



# 🎯 Objetivo do Projeto

Este projeto não é apenas uma ferramenta, mas um **exemplo prático** de como a **IA generativa** pode ser utilizada para transformar **imagens estáticas** em **vídeos dinâmicos**. Ele foi projetado para **entusiastas** e **profissionais** que desejam explorar as possibilidades de IA generativa **sem complicações técnicas**.

Desenvolver este **front-end** foi um desafio interessante e gratificante, e espero que você aproveite tanto quanto eu ao usá-lo! 🎉

---

# 🌐 Portfólio & Contato

Sou um especialista em **IA generativa avançada** e sempre busco novos desafios e oportunidades de aprendizado. Você pode conferir mais sobre meu trabalho e projetos em andamento nos links abaixo:

- **LinkedIn**: [Elias Andrade](https://www.linkedin.com/in/itilmgf/)
- **GitHub**: [Meu Repositório](https://github.com/chaos4455/)

---

# 🚀 Vamos Criar Algo Incrível Juntos!

Se você está interessado em **IA generativa** e quer explorar mais, **não hesite em me contatar** no meu linkedin🌟

**Vamos juntos descobrir ainda mais aplicações pra tecnologias de IA generativa!** 💪🎥✨

Maringá 26 08 2024 - Elias Andrade
