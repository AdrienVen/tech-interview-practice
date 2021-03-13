# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 23:54:05 2021

@author: adven
"""
def compress(string):
    
    chars = [i.lower() for i in string]
    
    "Our condition for appending compressed letters doesn't work in case"
    "chars[len(chars)-1] == chars[len(chars)-2]"
    "append none to the list of chars so this never happens."
    chars.append(None)
    i = 1
    
    "Keeps count of how many times we have seen a char"
    count = 1
    compressed = []
    while i < len(chars):
        if chars[i] == chars[i-1]:
            count += 1
        elif count > 1:
            compressed.append(chars[i-1])
            compressed.append(str(count))
            count = 1
            
        else:
            compressed.append(chars[i-1])
            count = 1
        i+=1
    print(compressed)
            
    if len(compressed) >= len(string):
        return string
    else:
        return compressed
    
"Runtime O(n)"
    
compress("aaaaaabbbbbbbbbccccc")