#!/usr/bin/env python

def primefactor():

    solve = 600851475143
    prime = False

    while prime == False:
        solve2 = solve / 2
        if type(solve2) == 'float' or solve2 % 2 != 0:
            print(solve2)
            break
        else:
            continue

primefactor()