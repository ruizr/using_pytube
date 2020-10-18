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

print('Videos in playlist: ' + TOTAL_PLAYLIST)

# physically downloading the audio track
#for video in playlist.video_urls:
#    print(video)

for index, row in df_playlist.iterrows():
    yt=YouTube(row['URLs'])
    streamName=yt.title
    streamName=streamName.replace('\'','')
    streamName=streamName.replace('.','')
    toFileName=DOWNLOAD_DIR + '/' + streamName + '.mp4'
    mp4file = Path("/path/to/file")
    if(mp4file.exists()):
        df_playlist.drop(index)

print('Total to download: ' + str(df_playlist.shape[0]))
print(df_playlist)

still_pending=df_playlist[df_playlist['Estado'].str.contains('NO_OK')]
pending=still_pending.shape[0]

while pending > 0:
    for index, row in df_playlist.iterrows():
        try:
            existsFile=False
            yt=YouTube(row['URLs'])
            streamName=yt.title            
            if(row['Estado']=='NO_OK'):
                if(detectedScrapping==True):
                    timeWait=random.randint(3,13)
                    print('Detected...waiting for ' + str(timeWait) + ' secs...')
                    time.sleep(timeWait)
                audioStream = yt.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
                audioStream.download(output_path=DOWNLOAD_DIR)
                df_playlist.at[index,'Estado']='OK'
                still_pending=df_playlist[df_playlist['Estado'].str.contains('NO_OK')]
                print('Pending to download: ' + str(still_pending.shape[0]))
                detectedScrapping=False
            else:
                detectedScrapping=False
                print('List completed...')
                break
                #continue

        except:
            print('Error with ' + str(row))
            yt=YouTube(row['URLs'])
            streamName=yt.title
            print(streamName)
            os.system('curl -I -s ' + row['URLs'] + ' -4')
            still_pending=df_playlist[df_playlist['Estado'].str.contains('NO_OK')]
            print('In error...Pending to download: ' + str(still_pending.shape[0]))
            print(still_pending)
            detectedScrapping=True
            timeWait=random.randint(3,5)
            time.sleep(timeWait)
            index=index+1
            continue

print('Download Complete')

#for video in playlist.videos:
    #print('Downloading ' + str(COUNTER) + ' of ' + TOTAL_PLAYLIST)
    #audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    #audioStream.download(output_path=DOWNLOAD_DIR)
    #COUNTER=COUNTER+1
    #time.sleep(1)