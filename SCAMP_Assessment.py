#!/usr/bin/env python
from getpass import getuser as user

fib = [ ]

try:
    n = input("Enter the number of alues you want in your sequence: ")
    n = int(n)
    if n < 1:
        n = input("Please enter a value greater than zero: ")
        n = int(n)
except ValueError:
    n = input("Please enter a positive integer value: ")
    n = int(n)


def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        fib.append(a)
    else:
        fib.append(a)
        fib.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            fib.append(c)

            
fibonacci(n)

print("""\nHello, {}! \n I'm glad you decided to run my code on the 
Fibonacci sequence. \n""".format(user()))

print(f"Your requested fibonacci sequence with {n} term is: {fib} ")
