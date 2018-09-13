#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def is_palindrome(start, end, arr):
    a = arr[start]
    while(start<end):
        if(arr[start] == a and a == arr[end]):
            start += 1
            end -= 1
            continue
        else:
            return False
    return True

def substrCount(n, arr):
    count = 0
    for i in range(1, len(arr)):
        start = 0
        end = i
        while(end < len(arr)):
            if(is_palindrome(start, end, arr)):
                count += 1
            
            start += 1
            end += 1
    return len(arr) + count
            
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
