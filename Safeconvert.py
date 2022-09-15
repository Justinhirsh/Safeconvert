import os, time, ctypes, sys,ffmpy,shutil
from pytube import YouTube
from tkinter import filedialog

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Welcome to Safeconvert")
    format = input("Please enter your desired format (ex: mp3 for audio or mp4 for video): ")
    type_of_vid = input("Please enter if your video is a video or audio: ")
    desired_video = input("please input the link to your desired video: ")
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
        inputs={os.path.dirname(yt.title + ".mp4") + yt.title + ".mp4": None},
        outputs={os.path.dirname(yt.title + ".mp4") + yt.title + format: None}
    )
    ff.run()
    os.remove(os.path.dirname(yt.title + ".mp4") + yt.title + ".mp4")
    shutil.move(os.path.dirname(yt.title + ".mp4") + yt.title + format, download_path)
    print("Complete!")
    time.sleep(1000)
    input("")


else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
is_admin()


