# Aplicativo que conter videos do Youtube em mp3
Esta é um projeto que converte videos do Youtube em mp3, para utizar basta seguir o seguintes passos:

## 1. Clone o repositorio.
:~$ git clone https://github.com/HelderMenegatti/youtube_video_convert_mp3.git

## 2. Ambiente virtual.
É recomendado a istalação das dependencias em um ambiente virtual, neste exemplo iremos utilizar o virtuaenv, dentro do repositorio que foi clonado crei o ambiente virtual.

:~$ virtuaenv nome_do_ambiete_virtual

## 3. Acessando o ambiente virtual.
para acessar o virtualenv basta utilizar o seguinte comando:

:~$ source nome_do_ambiete_virtual/bin/activate

## 4. Instalando as dependencias.
Dentro do ambiente viertual agora podemos instalar as dependencias do projeto:

:~$ pip3 install -r requiremens.txt

## 5. Inserindo o link(s) para processamento.

Dentro do arquivo download_video.py temos uma lista "urls = []" aqui vc pode inserir os link(s) que desejar baixar.

urls = [

  "https://www.youtube.com/watch?v=W8w-wlQsEJs&list=RDW8w-wlQsEJs&start_radio=1",
  ...demais links
]

## 6. Rodando a aplicação.
Agora basta rodar o arquivo no terminal:

python3 download_video.py


