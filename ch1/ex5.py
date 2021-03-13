# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:46:42 2021

@author: adven
"""
def one_away(str1, str2):
    
    
    diff = len(str1) - len(str2)
    if abs(diff) > 1:
        "if the difference in length is more than 1, the strings can't be one edit away."
        return False
    else:
        chars1 = [i.lower() for i in str1 if (i != " ")]
        chars2 = [i.lower() for i in str2 if (i != " ")]
        i = 0
        j = 0
        edits = 0

        while i < len(str1) and j < len(str2):
            if chars1[i] != chars2[j]:
                "if the characters don't match and:"
                
                if diff > 0:
                    "string 1 is the longest, then chars1[i] must be missing from"
                    "string 2, and chars1[i+1::] == chars2[j::]"
                    
                    i+=1
                    edits+=1
                elif diff < 0:
                    "string 2 is the longest, then chars2[j] must be missing from"
                    "string 1, and chars2[j+1::] == chars1[i::]"
                    
                    j+=1
                    edits+=1
                elif diff == 0:
                    "string 1 and 2 have the same length, then the two chars"
                    "are just different, and chars1[i+1::] == chars2[j+1::]"
                    
                    j+=1
                    i+=1
                    edits+=1
            else:
                j+=1
                i+=1   
            if edits > 1:
                return False
        return True
"Runtime O(n)"

print(one_away("pale", "bake"))
