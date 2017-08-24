import cv2
imagePath = "banana2.jpg"
cascPath = "banana.xml"
# http://alereimondo.no-ip.org/OpenCV/34

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=3,
    minNeighbors=2
    #minSize=(30, 30)
    #flags = cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image', 1000,750)
cv2.imshow("image",image)
cv2.waitKey(0)

