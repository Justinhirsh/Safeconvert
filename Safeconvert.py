import time
from pytube import YouTube
import os
from tkinter import filedialog
print("Welcome to Safeconvert")
format = input("Please enter .mp3 or .mp4: ")
if format == ".mp3":
    desired_video = input("please input the link to your desired video: ")
    yt = YouTube(desired_video)
    stream = yt.streams.filter(only_audio=True).first()
    print("downloading " + yt.title)
    download_path = filedialog.askdirectory()
    out_file = stream.download(output_path=download_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("Complete!")
    time.sleep(1000)
else:
    if format == ".mp4":
        desired_video = input("please input the link to your desired video: ")
        yt = YouTube(desired_video)
        stream = yt.streams.get_by_itag(22)
        print("Downloading "+yt.title)
        download_path = filedialog.askdirectory()
        stream.download(output_path=(download_path))
        print("Complete!")
        time.sleep(1000)
    else:
        if not format == ".mp3" or ".mp4":
            print("not valid format, please enter .mp3 or .mp4")
