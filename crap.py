import os
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1e64
prefix1 = "/dellfsqd2/medical/chuzhaobin/00.DLBCL/3.IF/orig.gray/" + sys.argv[1] + "/" + sys.argv[1]
prefix = "/dellfsqd2/medical/chuzhaobin/00.DLBCL/3.IF/crap/" + sys.argv[1] + "/" + sys.argv[1]
os.mkdir("/dellfsqd2/medical/chuzhaobin/00.DLBCL/3.IF/crap/" + sys.argv[1])

r_img = Image.open(prefix1 + "_r.CD20.png")
g_img = Image.open(prefix1 + "_g.CD3.png")

w, h = r_img.size
part = h // 5000
for i in range(0, part + 1):
    j = (1+i) * 5000
    if j > h: j = h
    box = (0, i*5000, w, j)
    r_img.crop(box).save(prefix + "_part" + str(i + 1) + "_r.CD20.png")
    g_img.crop(box).save(prefix + "_part" + str(i + 1) + "_g.CD3.png")
