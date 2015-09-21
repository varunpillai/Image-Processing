import cv2
import urllib
import numpy as np
import requests

# req = urllib.urlopen('https://s0.2mdn.net/viewad/4346663/Alex_300x250_webinar.jpg')
# arr = np.asarray(bytearray(req.read()), dtype=np.uint8)

req = requests.get('https://s0.2mdn.net/viewad/4532379/160x600_StateIncomeTax.jpg')
arr = np.asarray(bytearray(req.content), dtype=np.uint8)

img = cv2.imdecode(arr,-1) # 'load it as it is'

# cv2.imshow('lalala',img)
# if cv2.waitKey() & 0xff == 27: quit()

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Read the image
# image = cv2.imread(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))


