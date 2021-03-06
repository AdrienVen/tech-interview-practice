# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:27:13 2021

@author: adven
"""
from random import randint
random_string1 = [chr(randint(97,122)) for i in range(randint(5,7))]
random_string2 = [chr(randint(97,122)) for i in range(randint(5,7))]

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        "Create two arrays to store how many times a character appears in its string"
        "based on its ascii value"
        solution_array1 = [None]*94
        solution_array2 = [None]*94
        for i in range(len(str1)):
            if solution_array1[ord(str1[i])-32] == None:
                solution_array1[ord(str1[i])-32] = 1
            else:
                solution_array1[ord(str1[i])-32] += 1
            
            if solution_array2[ord(str2[i])-32] == None:
                solution_array2[ord(str2[i])-32] = 1
            else:
                solution_array2[ord(str2[i])-32] += 1
        
        "if the strings are permutations, then the arrays should be identical"
        for i in range( len( solution_array1)):
            if solution_array1[i] != solution_array2[i]:
                return False
        return True
    
"Running time O(n)"

#check_permutation(random_string1, random_string2)

#check_permutation("abcd","acdb")