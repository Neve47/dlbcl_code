import sys

data = []
with open(sys.argv[1], "r") as f1:
    for i in f1:
        data.append(i.strip().split(" "))

coordir = {}

for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == "0":
            continue
        cellid = "cell_" + sys.argv[3].split("_")[1] + "_" + data[i][j]
        if cellid not in coordir:
            coordir[cellid] = [[i, j]]
        else:
            coordir[cellid].append([i, j])

with open(sys.argv[2], "w") as f1:
    for i in coordir:
        print(i, end="\t", file=f1)
        for j in coordir[i]:
            print(str(j[0]) + "," + str(j[1]), end="\t", file=f1)
        print(file=f1)

