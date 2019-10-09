# -*- coding: utf-8 -*-
import cv2
import numpy as np

data=cv2.imread("images.jpg",0)
cv2.imwrite("daredevilgry.jpg",data)
print(type(data))
cv2.imshow("resim",data)
print(data.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
