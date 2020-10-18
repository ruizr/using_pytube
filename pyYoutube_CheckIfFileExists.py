from pathlib import Path
import random
import os
import subprocess
import re
import time
import pandas as pd
from pytube import Playlist
from pytube import YouTube

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = '/home/rodrigo/Music/YouTube/MusicMix'
COUNTER=1
TOTAL_PLAYLIST=0
lstEstado=[]
detectedScrapping=False
streamName=''

playlist = Playlist('https://www.youtube.com/playlist?list=PLq_ynTbfBtmn4zZTh2S-PwC8R9DCmjkay')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

df_playlist=pd.DataFrame(playlist.video_urls, columns=['URLs'])
TOTAL_PLAYLIST=str(df_playlist.shape[0])

for i in range(0,df_playlist.shape[0]):
    lstEstado.append('NO_OK')

df_playlist['Estado']=lstEstado
#print(df_playlist)

print('Total videos in playlist: ' + TOTAL_PLAYLIST)

for index, row in df_playlist.iterrows():
    yt=YouTube(row['URLs'])
    streamName=yt.title
    streamName=streamName.replace('\'','')
    streamName=streamName.replace('.','')
    toFileName=DOWNLOAD_DIR + '/' + streamName + '.mp4'
    #print('Checking if filename ' + toFileName + ' exists previously...')
    mp4file = Path("/path/to/file")
    if(mp4file.exists()):
        print('File: ' + toFileName + ' exists, so removing from dataframe...')
        df_playlist.drop(df_playlist.index)
        print(df_playlist.shape[0])
        

print('Total to download: ' + str(df_playlist.shape[0]))
print(df_playlist)