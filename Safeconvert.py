import time
from pytube import YouTube
import os
from tkinter import filedialog
print("Welcome to Safeconvert")
type_of_vid = input("Please enter audio or video depending on what kind of file you want: ")
format = input("Please enter your desired format (ex: .mp3 for audio or .mp4 for video): ")

if type_of_vid == "audio" or "Audio":
    desired_video = input("please input the link to your desired video: ")
    yt = YouTube(desired_video)
    stream = yt.streams.filter(only_audio=True).first()
    print("downloading " + yt.title)
    download_path = filedialog.askdirectory()
    out_file = stream.download(output_path=download_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + format
    os.rename(out_file, new_file)
    print("Complete!")
    time.sleep(1000)

else:
    if type_of_vid == "video" or "Video":
        desired_video = input("please input the link to your desired video: ")
        yt = YouTube(desired_video)
        print("downloading " + yt.title)
        download_path = filedialog.askdirectory()
        stream = yt.streams.filter().first()
        out_file = stream.download(output_path=download_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + format
        os.rename(out_file, new_file)
        print("Complete!")
        time.sleep(1000)
    else:
        print("you entered" + type_of_vid + ",please enter video or audio")
