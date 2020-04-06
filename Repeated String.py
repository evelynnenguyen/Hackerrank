#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    x = n % len(s)
    y = n // len(s)
    for i in range(len(s)):
        if s[i] == 'a':
            count += 1
    result = count * y
    
    count1 = 0
    xstr = s[:x]
    for cha in xstr:
        if cha == 'a':
            count1 += 1
            
    result += count1
    return result

if __name__ == '__main__':
    s = 'aba'
    n = 10
    result = repeatedString(s, n)
    print(str(result) + '\n')
