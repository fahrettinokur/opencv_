# -*- coding: utf-8 -*-
import cv2
import numpy as np

data=cv2.imread("tonystark.jpg")

b,g,r=cv2.split(data)
yeni_resim=cv2.merge((b,g,r))

data[:,:,0]=255 #sadace mavi tonlar 255  0 yerine 1 yaparsan yeşil olur
cv2.imshow("asil resim",data)
cv2.imshow("asil resim1",yeni_resim)

#cv2.imshow("Blue resim",b)
#cv2.imshow("Green resim",g)
#cv2.imshow("Red resim",r)



liste=[1,2,3]#yukardaki b g r mantığı

a,b,c=liste
print(b)
cv2.waitKey(0)
cv2.destroyAllWindows()