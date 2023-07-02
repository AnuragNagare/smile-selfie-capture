import cv2

video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Could not open video capture.")
    exit()

faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("dataset/haarcascade_smile.xml")

cnt = 1

while True:
    success, img = video.read()
    if not success:
        print("Failed to read frame from video capture.")
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)

    keyPressed = cv2.waitKey(1)
    if keyPressed & 0xFF == ord('q'):
        break

    for x, y, w, h in faces:
        img_with_faces = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 3)
        roi_gray = grayImg[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smiles = smileCascade.detectMultiScale(roi_gray, 1.8, 15)

        for sx, sy, sw, sh in smiles:
            img_with_smile = cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (100, 100, 100), 5)
            print("Image " + str(cnt) + " saved")
            path = "D:/Photos/Photo shoot/DSC_0207.JPG" + str(cnt) + ".jpg"
            cv2.imwrite(path, img_with_smile)
            cnt += 1

            if cnt >= 503:
                break

    cv2.imshow('Live Video', img)

video.release()
cv2.destroyAllWindows()
