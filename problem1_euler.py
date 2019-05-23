#!/usr/bin/env python

def multiples3and5():

        mult = []

        for num in range(1000):
                if num not in mult and num % 3 == 0:
                        mult.append(num)
                if num not in mult and num % 5 == 0:
                        mult.append(num)
        print(sum(mult))

multiples3and5()    