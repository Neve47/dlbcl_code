import sys
import  numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1e64

coordir = {}

with open(sys.argv[1], "r") as f1:
    for i in f1:
        line = i.strip().split("\t")
        coordir[line[0]] = line[1:]

cd20_density = {}
cd3_density = {}
r_img = Image.open(sys.argv[2])
g_img = Image.open(sys.argv[3])
cd20_arr = np.array(r_img)
cd3_arr = np.array(g_img)

coor_mm = {}
for cell in coordir:
    cd20_density[cell] = [0] * 256
    cd3_density[cell] = [0] * 256
    for coor in coordir[cell]:
        x = int(coor.split(",")[0])
        y = int(coor.split(",")[1])
        cd20_density[cell][cd20_arr[x][y]] += 1
        cd3_density[cell][cd3_arr[x][y]] += 1
        if cell not in coor_mm:
            coor_mm[cell] = [x, x, y, y]
            #xmin xmax ymin ymax
        else:
            if x < coor_mm[cell][0]: coor_mm[cell][0] = x
            if x > coor_mm[cell][1]: coor_mm[cell][1] = x
            if y < coor_mm[cell][2]: coor_mm[cell][2] = y
            if y > coor_mm[cell][3]: coor_mm[cell][3] = y

with open(sys.argv[4], "w") as f1:
    for i in cd20_density:
        print(i, file=f1, end=",")
        for j in cd20_density[i]:
            print(j, file=f1, end=",")
        print(file=f1)

with open(sys.argv[5], "w") as f1:
    for i in cd3_density:
        print(i, file=f1, end=",")
        for j in cd3_density[i]:
            print(j, file=f1, end=",")
        print(file=f1)

with open(sys.argv[6], "w") as f1:
    for cell in coordir:
        print(cell, sys.argv[7].split("/")[0], len(coordir[cell]), np.mean(cd20_density[cell]), np.mean(cd3_density[cell]), coor_mm[cell][0], coor_mm[cell][1], coor_mm[cell][2], coor_mm[cell][3], sep="\t", end="\n", file=f1)


