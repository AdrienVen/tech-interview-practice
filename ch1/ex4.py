# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:17:41 2021

@author: adven
"""
def palindrome_permutation(string):
    char_list = [i.lower() for i in string if (i != " ")]
    if len(char_list) % 2 == 0:
        return False
    else:
        "create an array to count the freq of each character in the string"
        solution_array = [0]*94
        for i in range(len(char_list)):
            if solution_array[ord(char_list[i])-32] == 0:
                solution_array[ord(char_list[i])-32] = 1
            else:
                solution_array[ord(char_list[i])-32] += 1
        solution_array = [i for i in solution_array if (i != 0)]
        
        "By definition palindromes have n pairs of chars and 1 singular char"
        single_found = False
        for i in solution_array:
            "if we have already found the singular char and we find another one,"
            "return false"
            if i % 2 == 1 and single_found:
                return False
            if i% 2 == 1:
                single_found = True
        "If the loop terminates, the string is a perm of a palindrome"
        return True

"Runtime: O(n)"
print(palindrome_permutation("Tact Coa"))