from pytube import YouTube
from pytube.cli import on_progress
from pydub import AudioSegment
import os, re

def get_mp4(url, path="./data/video/"):
    video_id = url.split("=")[-1]
    ytvideo = YouTube(url, on_progress_callback=on_progress)
    if (re.sub(r'\W+', '', video_id) + ".mp4") in os.listdir(path):
        print("File already exists: " + video_id)
        return
    print("Downloading mp4")
    ytvideo.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution().download(filename=f'{video_id}.mp4', output_path=path)
    print("\nFinish downloaded: " + video_id)
    # want_rename = input("rename file [Y]/n: ")
    # if want_rename == "n":
    #     return
    # else:

def get_mp3(url, path = "data/audio"):
    yt = YouTube(url)
    if (re.sub(r'\W+', '', yt.title) + ".mp3") in os.listdir(path):
        print("File already exists: " + yt.title)
        return
    print("Downloading mp3: " + yt.title)
    mp3 = yt.streams.filter(only_audio = True).first().download(path)
    # print("Finish downloaded: " + yt.title)
    want_rename = input("rename file [Y]/n: ")
    if want_rename == "n":
        return
    else:
        file_name = input("Enter the new file name: ")
        os.rename(mp3, path + "/" + file_name + ".mp3")

def split_mp3(path = "data/audio", size = 5000):
    for each_mp3 in os.listdir(path):
        if each_mp3.endswith(".mp3"):
            change_file_type = input(f"Change {each_mp3} file type [Y]/n : ")
            if change_file_type == "n":
                file_type = "mp3"
            else:
                file_type = input("Enter the new file type: ")
            audio = AudioSegment.from_file(path + "/" + each_mp3)
            file_num = 0
            while len(audio) > size:
                print("Splitting: " + each_mp3 + " -  downloaded " + str(file_num) + '\t/  queue ' + str(len(audio) // size))
                chunk = audio[:size]
                audio = audio[size:]
                chunk.export(path + "/" + each_mp3.replace('.mp3', '') + ' - ' + str(file_num) + f".{file_type}", format = f"{file_type}", parameters = ["-ar", "16000"])
                file_num += 1