# Returns the text in each advertisement
__author__ = 'Varun'
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import requests
from StringIO import StringIO
import re

i = 0
f = open('urls.txt', 'r')
out = open('action.txt', 'w')

for line in f:
    i += 1
    response = requests.get(line)
#  print response.status_code, "\t", line
    img = Image.open(StringIO(response.content))

# GET TEXT FROM THE IMAGES
#    val = str(i) + ":" + line + "\t" + pytesseract.image_to_string(img) + "\n"
    strng = pytesseract.image_to_string(img)
    pattern = re.compile('\W')

    val = re.sub(pattern, '', strng)
# Our string to search, and the substring searches.
    search_strs = ('ACT', 'CLICK', 'LEARN', 'SAVE', 'FREE', 'SEND')

# Case insensitive search.
    val_lower = val.lower()
    action_fnd = "F"
    for search_str in search_strs:
        if search_str.lower() in val_lower:
            action_fnd="T"
            break

    print str(i) +" "+ action_fnd
    val = str(i)+ "\t" + action_fnd + ": " + line
    out.write(val)

f.close()
out.close()

# SPELL CHECK EACH LINE

# SPELL CORRECT EACH WRONG WORD