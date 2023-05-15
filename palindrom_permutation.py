"""
Write a Python program that accepts a string and determines whether the string can form a palindrome. 
A string can form a palindrome if its characters can be arranged in such a way that it forms a word that can be read the same way backwards. 
Example: "civic" and "ivicc" are two examples of strings that can form a palindrome.
"""

def check_string(string1: str, string2: str):
    palindrome = True
    if len(string1) == len(string2):
        for char1 in string1:
            if char1 in string2:
                char1_count = string1.count(char1)
                char2_count = string2.count(char1)
                if char1_count == char2_count:
                    continue
                else:
                    palindrome = False
                    break
    else:
        palindrome = False
    
    return palindrome


print(check_string('civic', 'ivicc'))

