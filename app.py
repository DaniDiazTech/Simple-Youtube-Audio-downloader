'''App to download mp3 audio'''
from youtube_dl import YoutubeDL

from utils import get_url_input, ydl_opts

if __name__ == '__main__':

    audio_downloader = YoutubeDL(ydl_opts)

    url = get_url_input('Enter your URL: ')
    
    with YoutubeDL(ydl_opts) as ydl:

        ydl.download([url])