import os, time,ffmpy,shutil
import pathlib
from pytube import YouTube
from pytube import Playlist
from tkinter import filedialog


print("Welcome to Safeconvert")
format = str(input("Please enter your desired format (ex: mp3 for audio or mp4 for video): "))
type_of_vid = input("Please enter if your video is a video or audio: ")
desired_video = input("please input the link to your desired video or playlist: ")
is_playlist = input("are you converting a video or playlist: ")
dir_path = str(pathlib.Path(__file__).resolve().parent) + "\\"
forbiden_characters = str("/, \, <, >, :, \", |, ?, *, '")
if is_playlist == "playlist":
    p = Playlist(desired_video)
    download_path = filedialog.askdirectory()
    print("downloading playlist")
    for yt in p.videos:
        if type_of_vid == "audio" or "Audio":  
            yt.streams.filter(only_audio= True, bitrate= 320, resolution= 1080)
        else:
            yt.streams.filter(bitrate= 320, resolution= 1080)
        print("filtered " + yt.title)  
    for video in p.videos:
        name = video.title.replace(" ", "_")
        if forbiden_characters in name:
            name = name.replace(forbiden_characters, "")
        video.streams.first().download(filename= name)
        os.rename(name, name + ".mp4")
        print("processed " + name)
    print("finished processing")
    
    for video in p.videos:
        name = video.title.replace(" ", "_")
        if name in forbiden_characters:
            name = name.replace(forbiden_characters, "")
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
    if forbiden_characters in yt.title:
        yt.title = yt.title.replace(forbiden_characters, "")
    print("downloading " + yt.title)
    download_path = filedialog.askdirectory()
    if type_of_vid == "audio" or "Audio":
        stream = yt.streams.filter(only_audio= True).first()
    else:
        stream = yt.streams.filter().first()
    stream.download()
    try:
        ff = ffmpy.FFmpeg(
            inputs={dir_path + yt.title + ".mp4": None},
            outputs={dir_path + yt.title + format: None}
        )
        ff.run()
    except:
        print("conversion failed, could be due to file format already being .mp4")
    os.remove(dir_path + yt.title + ".mp4")
    shutil.move(dir_path + yt.title + format, download_path)
    print("Complete!")
    time.sleep(1000)
   


