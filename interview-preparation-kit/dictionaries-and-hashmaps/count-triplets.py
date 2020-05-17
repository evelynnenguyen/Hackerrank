#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r, n):
    t = 0
    r = float(r)
    return t

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        nr = input().rstrip().split()

        n = int(nr[0])
        # print('n', n)
        r = int(nr[1])
        # print('r', r)
        arr = list(map(int, input().rstrip().split()))
        print('arr', arr)
        ans = countTriplets(arr, r, n)
        print(ans)
