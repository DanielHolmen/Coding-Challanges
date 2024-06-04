# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:18:03 2024

@author: dehol
"""

word_list = ["potato", "soup", "flick", "jesus", "tomato"]

flicked = False

for word in word_list:
    if word == "flick":
        flicked = True
        print("False")
    else:
        if flicked:
            print("False")
        else:
            print("True")
        

