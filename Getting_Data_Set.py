import hashlib
from random import *
import csv
rockyou = open("<path to rockyou>/rockyou.txt", "r")
x = []
hashname =["md5", "sha256", "sha512"]
itr = 0
for i in range(0, 100):
    if (rockyou.readline(i)[0:-1] == "") or (rockyou.readline(i)[0:-1] == " ") :
        continue
    else:
        x.append([rockyou.readline(i)[0:-1],sample(hashname,1)[0]])
        if x[itr][1] == "md5":
            tempvari = hashlib.md5(x[itr][0].encode())
        elif x[itr][1] == "sha256":
            tempvari = hashlib.sha256(x[itr][0].encode())
        elif x[itr][1] == "sha512":
            tempvari = hashlib.sha512(x[itr][0].encode())

        x[itr].append(tempvari.hexdigest())
        itr+=1

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(x)
