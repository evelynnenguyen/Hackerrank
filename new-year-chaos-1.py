#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    count = 0
    flag = True
    for i in range(n-1, -1, -1):
        # print('i', i)
        if q[i] - i > 3:
            flag = False
            break
        if q[i] != (i+1):
            if q[i-1] == (i+1):
                count += 1
                q[i], q[i-1] = q[i-1], q[i]
            elif q[i-2] == (i+1):
                count += 2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1], q[i] = q[i], q[i-1]

    if flag == True:
        print(count)
    else:
        print("Too chaotic")

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
