#!/usr/bin/env python

# Maybe not the most elegant, but it does the trick

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

evens = []

for num in list(fib(34)):
    if num not in evens and num < 4000000 and num % 2 == 0:
        evens.append(num)

print(sum(evens))

