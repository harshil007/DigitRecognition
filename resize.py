import os
from PIL import Image
import numpy as np


def resize(infile):
    size = 28, 28

    outfile = "/images/converted/" + os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im = im.resize(size, Image.ANTIALIAS)
            #im.thumbnail(size, Image.ANTIALIAS)
            im = im.convert('LA')
            im.save(outfile, "PNG")

        except IOError:
            print("cannot create thumbnail for '%s'" % infile)

    return outfile
