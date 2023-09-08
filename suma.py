# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
NUM = 8 
NUMS = [0]*NUM
total = 0
for i in range(NUM):
    NUMS[i]=int(input("Introduzca el número: "))
    total += NUMS[i]
    print("El total es : ", total)