import os
import re
from pytube import YouTube
from moviepy.editor import *

urls = [
# ...
]


def  checks_for_duplicate_items(lista):
    count = []
    for item in lista:
        if item in count:
            continue
        else:
            count.append(item)
    print(f"-- lista bruta {len(lista)} -- lista tratada {len(count)}")
    return count


def remover_caracteres_nao_permitidos(nome_arquivo):
    # Define a expressão regular para encontrar caracteres não permitidos
    regex = r"[\\/:*?\"<>|\n\t]"  # Adicione aqui os caracteres que deseja remover
    nome_arquivo_sem_caracteres_nao_permitidos = re.sub(regex, "", nome_arquivo)
    return nome_arquivo_sem_caracteres_nao_permitidos


def download_video_and_convert(url):
    try:
        # Baixa o video do Youtube
        yt = YouTube(url)
        video_title = remover_caracteres_nao_permitidos(yt.title)
        # video_title = yt.title
        video_stream = yt.streams.filter(only_audio=True).first()
        temp_video_filename = f"{video_title}.mp4"
        video_stream.download(filename=temp_video_filename)
        
        # Converte o video para mp3
        video_clip = AudioFileClip(temp_video_filename)
        audio_filename = f"{video_title}.mp3"
        video_clip.write_audiofile(audio_filename)
        
        # Exclui o arquivo de video temporario
        os.remove(temp_video_filename)
        
        print("Download e converção concluidos!")
        print(f"O arquivo de audio '{audio_filename}' foi salvo com sucesso!!")
    except Exception as e:
        print("Ocorreu um erro:", str(e))


def convection_process(urls):
    validated_urls = checks_for_duplicate_items(urls)
    for url in validated_urls:
        download_video_and_convert(url)

    print("Lista de urls finalizada!!!")


convection_process(urls)
