# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:45:02 2021

@author: adven
"""

def urlify(string, length):
    "first find the index of the first character to get rid of leading space"
    first_char_index = 0
    while string[first_char_index] == " ":
        first_char_index +=1
        
    "slice the string with real length to get rid of trailing space"
    string = list(string[0:length])

    "iterate over the string"
    for i in range(length):
        if string[i] == " ":
            
            "if a space is found and next char is a space too, replace with empty char"
            if (i < length+1):
                if string[i+1] == ' ':
                    string[i] = ''
                else:
                    
                    "otherwise replace with %20"
                    string[i] = "%20"
                
    "return the joined string"
    return "".join(string)

"Runtime O(n)"