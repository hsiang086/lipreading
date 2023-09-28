import cv2


FACECASCADE = cv2.CascadeClassifier("./models/haarcascade_frontalface_alt.xml")
interval = 4
def get_img(path):
    cap = cv2.VideoCapture(path)
    i = 0
    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = FACECASCADE.detectMultiScale(gray, 1.7, 7)
        if len(face) == 1:
            for (x, y, w, h) in face:
                if i % interval == 0:
                    cv2.imwrite("./face-rec/images/zhiqi-" + str(idx) + ".jpg", frame[y - 40:y + h + 20, x - 20:x + w + 20])
                    idx += 1
                cv2.rectangle(frame, (x - 20, y - 40), (x + w + 20, y + h + 20), (0, 255, 0), 2)
        i += 1
        cv2.imshow('Video with Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


get_img("./data/video/F0iZyjDsMpM.mp4")