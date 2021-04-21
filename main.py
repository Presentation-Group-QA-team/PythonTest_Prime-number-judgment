  
# -*- coding: UTF-8 -*-
#BerNie_test
# Filename : test.py
# author by : www.twcode01.com 
# Python 程式用於檢測使用者輸入的數值是否為質數
 
# 使用者輸入數值
num = int(input("input number : "))
while(num >= 0):
# 質數大於 1
  if num > 1:
   # 檢視因子
   for i in range(2,num):
    if (num % i) == 0:
      num1 = num%i
      print(num,"不是質數")        
      print(i,"X",num//i,"=",num)
      num = int(input("input number : "))
      break
    else :
      print(num,"是質數")
      num = int(input("input number : "))
      break
    