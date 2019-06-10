#!/usr/bin/env python

def palindrome():

    # create a list to store palindromes
    palindromes = []

    for x in range(100, 999):
        for y in range(100, 999):
            value = x * y
            if str(value) == str(value)[::-1]:
                palindromes.append(value)
            else:
                continue
    print(max(palindromes))

    
palindrome()
    

