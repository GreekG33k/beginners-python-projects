# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:26:33 2019

@author: S.Kaiafis

Challenge :
    Write a program that asks the user how many Fibonnaci numbers to generate,
    and then generates them.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the next number 
    in the sequence is the sum of the previous two numbers 
    in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate?: "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count -1 ):
            fib.append(fib[i] + fib[i-1])
            i += 1
    for num in fib:
        print (num)
    

gen_fib()


#print("\nIt's alive, it's ALIVE!!!")