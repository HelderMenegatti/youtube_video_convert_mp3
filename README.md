# Aplicativo para converter vídeos do Youtube em MP3
Este é um projeto que converte vídeos do Youtube em MP3. Para utilizá-lo, siga estes passos:

## 1. Clone o repositório.
:~$ git clone https://github.com/HelderMenegatti/youtube_video_convert_mp3.git

## 2. Ambiente virtual.
É recomendada a instalação das dependências em um ambiente virtual. Neste exemplo, utilizaremos o virtualenv. Dentro do repositório clonado, crie o ambiente virtual.

:~$ virtuaenv nome_do_ambiete_virtual

## 3. Acessando o ambiente virtual.
Para acessar o virtualenv, basta utilizar o seguinte comando:

:~$ source nome_do_ambiete_virtual/bin/activate

## 4. Instalando as dependências.
Dentro do ambiente virtual, agora podemos instalar as dependências do projeto:

:~$ pip3 install -r requiremens.txt

## 5. Inserindo o(s) link(s) para processamento.

Dentro do arquivo download_video.py, temos uma lista "urls = []". Aqui você pode inserir o(s) link(s) que deseja baixar.

urls = [

  "https://www.youtube.com/watch?v=W8w-wlQsEJs&list=RDW8w-wlQsEJs&start_radio=1",
  ...outros links
]

## 6. Executando a aplicação.
Agora, basta executar o arquivo no terminal:

python3 download_video.py
