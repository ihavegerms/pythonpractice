#!/usr/bin/env python

# comment your code better... can't explain why you did something 1 or 2 days later
def primefactor(a):
    b = 2
    while (a > b):
        if (a % b == 0):
            # i'm a derp i did this cause x,y
            a = a / b;
            # this causes x to happen cause y is dumb
            b = 2;
        else:
            b += 1;
    print(str(b))

primefactor(600851475143000000000000000000000)