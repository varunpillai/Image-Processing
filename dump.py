__author__ = 'Varun'
# Returns a file out2.txt with the filename URL and whether it has a human being in it
__author__ = 'Varun'
from PIL import Image
import requests
from StringIO import StringIO
import cv2
import numpy as np
import imghdr

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

response = requests.get('https://s0.2mdn.net/viewad/4240544/CMC_SeniorsAreDoneWatching_728x90.gif')

img = Image.open(StringIO(response.content))
val = img.format
mypalette = img.getpalette()
img.putpalette(mypalette)
frstframe = Image.new("RGBA", img.size)
frstframe.paste(img)
frstframe.save('dump.png')
# arr = np.asarray(frstframe, dtype=np.uint8)
# data = cv2.imdecode(arr,-1) # 'load it as it is'
image = cv2.imread('dump.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))

# if len(faces) > 0:
#  val = str(i)+ "\t" + "FF:" + line
# else:
#  val = str(i)+ "\t" + "NF:" + line
