# -*- coding: utf-8 -*-

import cv2
import numpy as np

data=cv2.imread("tonystark.jpg")
#deneme=data[50:1000,0:60]#►güzel ilerde kullanırsın
#cv2.imshow("deneme",deneme)

#print(data[50,50])
#print("Datanın Boyutu="+str(data.size))
#print("Datanın Özelliği="+str(data.shape))
#print("Datanın Bit değeri="+str(data.dtype))

cv2.imshow("değişmemiş tony",data)

for i in range(0,130):
    for t in range(150,289):
        data[i,t]=[255,0,0]


cv2.imshow("Değişmiş tony",data)






cv2.waitKey(0)
cv2.destroyAllWindows()