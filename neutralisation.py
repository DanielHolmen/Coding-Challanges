# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:33:57 2024

@author: dehol
"""

strings = {"++-+-": "-++--"}

new_string = ""

for a, b in strings.items():
    for i in range(len(a)):
        if a[i]==b[i]:
            new_string += a[i]
        else:
            new_string += "0"
            
print(new_string)