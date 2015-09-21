# Returns a file out2.txt with the filename URL and whether it is DARK or LIGHT
__author__ = 'Varun'
from PIL import Image
import requests
from StringIO import StringIO

i = 0
f = open('urls.txt', 'r')
out = open('out2.txt', 'w')

for line in f:
  i += 1
  response = requests.get(line)
  print response.status_code, "\t", line
  img = Image.open(StringIO(response.content))
  gsimg = img.convert(mode='L')
  hg = gsimg.histogram()
# count should be 256 most/all of the time (an index for each shade of grey)
  count = len(hg)
  if sum(hg[:count/2]) > sum(hg[count/2:]):
     val = str(i)+ "\t" + "DARK: " + line
  else:
     val = str(i)+ "\t" + "LIGHT: " + line

  out.write(val)

f.close()
out.close()