#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    s = 0
    l = len(arr)
    for i in range(l):
        while arr[i] != i+1:
            pos1 = i
            pos2 = arr[i]-1
            arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
            s += 1
    return s

if __name__ == '__main__':
    k = int(input())
    for j in range(k):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        res = minimumSwaps(arr)
        print(res)
