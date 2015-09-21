__author__ = 'Varun'
from PIL import Image
import sys

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print "Cant load", infile
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save(infile+str(i)+'.png')

    except EOFError:
        pass # end of sequence

processImage('1-04-McDaniel-300x250.gif')