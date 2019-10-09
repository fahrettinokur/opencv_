# -*- coding: utf-8 -*-
import cv2

data=cv2.imread("indir1.jpg")

#print(data)
cv2.imshow("Hayatı Inanc",data)#ver numpy olarak kaydediyor
print(data.size)
print(data.dtype)#8 bitlik olduğunu görürsün yani 1 1 1 1 1 1 1 1 =255 olur mantık o
print(data.shape)#(220,229,3) yükseklik genişlik renk
#print("değer görme=",data.item(100,100,2))# 0 blue 1 green 2 red
cv2.imwrite("hayati.jpg",data)
data2=cv2.imread("hayati.jpg",0)
print("BGR deki BLUE değeri=",data.item(110,90,0))
print("BGR deki GREEN değeri=",data.item(110,90,1))
print("BGR deki RED değeri=",data.item(110,90,2))


print("BGR deki BLUE değeri but gre resim=",data2.item(110,90),0)
print("BGR deki GREEN değeri but gre resim =",data2.item(110,200),1)
print("BGR deki RED değeri but gree resim=",data2.item(5,100),2)






cv2.waitKey(0)
cv2.destroyAllWindows()
