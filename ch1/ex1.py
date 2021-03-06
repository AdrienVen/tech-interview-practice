# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:52:45 2021

@author: adven
"""
import random
random_string = [chr(random.randint(97,122)) for i in range(3,random.randint(5,20))]
print(random_string)

def binary_search(char, lst):
    left = 0
    right = len(lst)-1
    while left <= right:
        middle = (left + right) //2
        if lst[middle] < char:
            left = middle + 1
        elif lst[middle] > char:
            right = middle - 1
        else:
            return True
    return False

"Determine if a list has all unique characters"
def is_unique(string):
    "1. sort the list"
    string.sort()
    
    "2. for each letter in the list, apply binary search"
    for i in range(len(string)):
        letter = string.pop()
        is_in_string = binary_search(letter, string)
        
        "3. If binary search returns True"
        if is_in_string == True:
            
            "3.1 return false"
            print(letter,"is in the string at least twice")
            return False
            
    "4 if we have reached the end return true"
    print("All characters are unique.")
    return True
"Runtime O(nlog(n))"

is_unique(random_string)