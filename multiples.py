#!/usr/bin/env python

def multiples(y):

        mult = []

        for x in range(1000):
                if x not in mult and x % int(y) == 0:
                        mult.append(x)

        print(mult)

multiples(3)