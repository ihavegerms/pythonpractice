#!/usr/bin/env python

a = 600851475143 

def primefactor(a):
    b = 2
    while (a > b):
        if (a % b == 0):
            a = a / b;
            b = 2;
        else:
            b += 1;
    print(str(b))

primefactor(a)