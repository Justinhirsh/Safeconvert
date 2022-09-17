
import os, time,ffmpy,shutil
import pathlib
from pytube import YouTube
from pytube import Playlist
from tkinter import filedialog


print("Welcome to Safeconvert")
format = input("Please enter your desired format (ex: mp3 for audio or mp4 for video): ")
type_of_vid = input("Please enter if your video is a video or audio: ")
desired_video = input("please input the link to your desired video or playlist: ")
is_playlist = input("are you converting a video or playlist: ")
if is_playlist == "playlist":
    p = Playlist(desired_video)
    download_path = filedialog.askdirectory()
    print("downloading playlist")
    dir_path = str(pathlib.Path(__file__).resolve().parent) + "\\"
    for video in p.videos:
        name = video.title.replace(" ", "_")
        video.streams.first().download(filename= name)
        os.rename(name, name + ".mp4")
        print("processed " + name)
    print("finished processing")
    
    for video in p.videos:
        name = video.title.replace(" ", "_")
        ff = ffmpy.FFmpeg(
            inputs={dir_path + name + ".mp4": None},
            outputs={dir_path + name + format: None}
        )
        ff.run()
        os.remove(dir_path + name + ".mp4")
        shutil.move(dir_path + name + format, download_path)
        print("downloaded " + name)
    print("complete!")
if is_playlist == "video":
    yt = YouTube(desired_video)
    yt.title = yt.title.replace(" ", "_")
    print("downloading " + yt.title)
    download_path = filedialog.askdirectory()
    if type_of_vid == "audio" or "Audio":
        stream = yt.streams.filter(only_audio= True).first()
    else:
        stream = yt.streams.filter().first()
    stream.download()
    ff = ffmpy.FFmpeg(
        inputs={os.path.dirname(yt.title + ".mp4"): None},
        outputs={os.path.dirname(yt.title + format): None}
    )
    ff.run()
    os.remove(os.path.dirname(yt.title + ".mp4"))
    shutil.move(os.path.dirname(yt.title + format), download_path)
    print("Complete!")
    time.sleep(1000)
   


