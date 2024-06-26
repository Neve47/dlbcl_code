import sys
from PIL import Image
from PIL import ImageDraw
import random
Image.MAX_IMAGE_PIXELS = None

r = Image.open(sys.argv[1])
g = Image.open(sys.argv[2])
b = Image.open(sys.argv[3])

img = Image.merge('RGB', (r, g, b))
a = ImageDraw.ImageDraw(img)

celllist = []
c1, c2 = 0, 0
with open(sys.argv[4], "r") as f1:
    for line in f1:
        bbox = line.strip().split("\t")
        cell = bbox[0]
        c1 += 1
        cd20 = float(bbox[3])
        cd3 = float(bbox[4])
        if (cd20 > 7) and (cd3 > 5):
            celllist.append(cell)
            c2 += 1
if c2 > (c1 / 4):
    celllist = random.sample(celllist, int(c1 / 4))

with open(sys.argv[5], "r") as f1:
    for line in f1:
        bbox = line.strip().split("\t")
        cell = bbox[0]
        if cell in celllist:
            x1=float(bbox[5])
            x2=float(bbox[6])
            y1=float(bbox[7])
            y2=float(bbox[8])
            a.rectangle(((y1, x1), (y2, x2)), fill=None, outline='white', width=5)

img.save(sys.argv[6], quality=95)


