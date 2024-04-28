import os
from pytube import YouTube
from moviepy.editor import *

urls = []

def download_video_and_convert(url):
    try:
        # Baixa o video do Youtube
        yt = YouTube(url)
        video_title = yt.title
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


for url in urls:
    download_video_and_convert(url)

print("Lista de urls finalizada!!!")