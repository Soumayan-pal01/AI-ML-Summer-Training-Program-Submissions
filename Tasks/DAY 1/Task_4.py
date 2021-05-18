# -*- coding: utf-8 -*-
"""
Created on Tue May 18 20:22:32 2021

@author: KIIT
"""
string = input("Enter the string:\n")
str1=''
str2=''
c=0
s=0
v=0
n=0
for char in string:
    if char in "aeiouAEIOU":
        str1=str1+char
        v=v+1
    elif char==' ':
        s=s+1
    elif char in "0123456789":
        n=n+1  
        str2=str2+char
    else:
        c=c+1
        
print("The vowels present the string are {0}".format(str1))
print("No. of vowels={}".format(v))    
print("No. of consonants={}".format(c))
print("No. of spaces={}".format(s))
print("The numericals present in the string are {0}".format(str2))
print("No. of numericals={}".format(n))      