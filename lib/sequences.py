#!/usr/bin/env python3

def print_fibonacci(length):
    i = 1
    num = 0
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    elif length > 2:
        while i < length:
            num_list = [0, 1]
            num_list.append(num_list[i]+num_list[i-1])
            i+=1
        print (num_list)