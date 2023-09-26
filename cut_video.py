import os
import cv2

FACECASCADE = cv2.CascadeClassifier("./models/haarcascade_frontalface_alt.xml")
def cut(path):
    cap = cv2.VideoCapture(path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = FACECASCADE.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Video with Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def main(path="./data/video/"):
    for file in os.listdir(path):
        if file.endswith(".mp4"):
            print(file)
            cut(path+file)

main()