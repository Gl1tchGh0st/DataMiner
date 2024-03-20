import cv2

def takePhoto():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        exit()
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't capture a frame.")
        exit()
    cap.release()
    cv2.imwrite("photo.png", frame)