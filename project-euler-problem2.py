#!/usr/bin/env python

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

evens = []

for num in list(fib(31)):
    if num % 2 == 0 and num not in evens:
        evens.append(num)

print(sum(evens))

