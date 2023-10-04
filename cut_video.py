from face_correction import run
import data.subtitles.subtitles as sub
import os
import cv2
import skvideo.io


FACECASCADE = cv2.CascadeClassifier("./models/haarcascade_frontalface_alt.xml")

def cut_video(path, subt, out_path="./data/cut_video/"):
    print("start cutting")
    input_video = skvideo.io.vread(path)
    for i in eval(subt):
        start_sec = i['start']
        end_sec = i['start'] + i['duration']
        frame_rate = skvideo.io.ffprobe(path)['video']['@r_frame_rate']
        frame_rate = eval(frame_rate)
        start_frame = int(start_sec * frame_rate)
        end_frame = int(end_sec * frame_rate)
        output_video = input_video[start_frame:end_frame]
        out_path_ = out_path + str(start_sec) + ".mp4"
        skvideo.io.vwrite(out_path_, output_video)
        print(f'mp4 output path: {out_path_}')


def get_dot(path):
    cap = cv2.VideoCapture(path)
    j = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = FACECASCADE.detectMultiScale(gray, 1.1, 7)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if len(face) != 0:
            run(j, imgarray = frame)
            j += 1
        cv2.imshow('Video with Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def main(path="./data/video/", video_id="znJbiTVg6_M"):
    for file in os.listdir(path):
        if file.endswith(".mp4"):
            print(file)
            cut_video(path + file, f"sub.{video_id}")
