# Returns a file out2.txt with the filename URL and whether it has a human being in it
__author__ = 'Varun'
from PIL import Image
import requests
from StringIO import StringIO
import cv2
import numpy as np

i = 0
f = open('urls.txt', 'r')
out = open('humn.txt', 'w')

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for line in f:
    i += 1
    response = requests.get(line)

# check if gif else process normally
    extn = line[len(line)-4:len(line)-1]
    img = Image.open(StringIO(response.content))

    if extn.lower() == 'gif' and img.format != 'JPEG':
        mypalette = img.getpalette()
        img.putpalette(mypalette)
        frstframe = Image.new("RGBA", img.size)
        frstframe.paste(img)
        frstframe.save('dump.png')
        image = cv2.imread('dump.png')
    else:
        arr = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(arr,-1) # 'load it as it is'

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print str(i), "Found {0} faces!".format(len(faces))

    if len(faces) > 0:
        val = str(i)+ "\t" + "FF:" + line
    else:
        val = str(i)+ "\t" + "NF:" + line

# write to output file
    out.write(val)

f.close()
out.close()