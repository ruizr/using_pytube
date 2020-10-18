from pytube import YouTube

#ask for the link from user
link = 'https://youtu.be/dzNztCuq6EM'
yt = YouTube(link)
YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = '/home/rodrigo/Music/YouTube/HipHop'

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
#ys = yt.streams.get_highest_resolution()
#ys=yt.streams.filter(type='video', subtype='mp4').order_by('resolution').desc().first()
#print(str(ys))

#for item in yt.streams.filter(type='video', subtype='mp4').order_by('resolution').desc().all():
    #print(item)

#Starting download
print("Downloading...")
#ys.download()
#yt.streams.filter(type='video', subtype='mp4').order_by('resolution').desc().first().download()  # SOLO BAJA EL VIDEO, SIN AUDIO
#yt.streams.order_by('resolution').desc().first().download()
audioStream = yt.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
audioStream.download(output_path=DOWNLOAD_DIR)
print("Download completed!!")