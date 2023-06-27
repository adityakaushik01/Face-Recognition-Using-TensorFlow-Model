import cv2
import os

video = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier('C:/Users/kadit/AppData/Roaming/Python/Python311/site-packages/cv2/data/haarcascade_frontalface_default.xml')

count = 0

nameID = str(input("Enter your name: ")).lower()

path = 'images/'+nameID

isExist = os.path.exists(path)

if isExist:
    print("Name Already Taken")
    nameID = str(input("Enter your name again: "))
else:
    os.makedirs(path)

while True:
    ret, frame = video.read()
    faces = facedetect.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        count = count+1
        name = './images/'+nameID+'/'+str(count)+'.jpg'
        print("Creating Images..........."+name)
        cv2.imwrite(name, frame[y:y+h, x:x+h])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Window Frame", frame)
    cv2.waitKey(1)
    if count>200:
        break
video.release()
cv2.destroyAllWindows()