#!/usr/bin/env python

def multiples(y):

        mult = []

        for x in range(1000):
                if x not in mult and x % int(y) == 0:
                        mult.append(x)
        
        sumMult = input('Would you like the sum of the multiples as well? [y/n] ')

        if sumMult.lower() == 'y':
            print(sum(mult))

        print(mult)

def multiples2(x,y):

        mult = []

        for num in range(1000):
                if num not in mult and num % x == 0:
                        mult.append(num)
                if num not in mult and num % y == 0:
                        mult.append(num)
        print(sum(mult))
        print(mult)


multiples(10)
multiples2(3,5)