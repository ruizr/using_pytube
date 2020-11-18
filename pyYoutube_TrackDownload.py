from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': 'True',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    },
    {'key': 'EmbedThumbnail'},
    {'key': 'FFmpegMetadata'}],
    'postprocessor_args': [
        '-ar', '16000', '-threads', '0 1'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/Xoz6l-COqxw'])