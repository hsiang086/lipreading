import tensorflow as tf
import numpy as np
import cv2

MODEL = tf.keras.models.load_model("./models/face_rec.h5")
FACECASCADE = cv2.CascadeClassifier("./models/haarcascade_frontalface_alt.xml")
FONT = cv2.FONT_HERSHEY_SIMPLEX

def run(path):
    cap = cv2.VideoCapture(path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        face = FACECASCADE.detectMultiScale(frame, 1.1, 5)
        if len(face) == 0:
            continue    
        for (x, y, w, h) in face:
            rect = frame[y - 40:y + h + 20, x - 20:x + w + 20] if y - 40 > 0 and x - 20 > 0 else frame[y:y + h, x:x + w]
            rect = cv2.resize(rect, (100, 100))
            rect = cv2.cvtColor(rect, cv2.COLOR_BGR2GRAY)
            print((MODEL(rect[None, ...])[0,0] >= 0.5).numpy())
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Video with Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def run_on_flask(path):
    # print(1234567890987654321)
    cap = cv2.VideoCapture(path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        face = FACECASCADE.detectMultiScale(frame, 1.1, 5)
        if len(face) == 0:
            continue    
        for (x, y, w, h) in face:
            rect = frame[y - 40:y + h + 20, x - 20:x + w + 20] if y - 40 > 0 and x - 20 > 0 else frame[y:y + h, x:x + w]
            rect = cv2.resize(rect, (100, 100))
            rect = cv2.cvtColor(rect, cv2.COLOR_BGR2GRAY)
            is_zhiqi = str((MODEL(rect[None, ...])[0,0] >= 0.5).numpy())
            cv2.putText(frame, is_zhiqi, (x, y), FONT, 1, (0, 255, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    print(1)
    cap.release()
    cv2.destroyAllWindows()

# run("./data/video/znJbiTVg6_M.mp4")