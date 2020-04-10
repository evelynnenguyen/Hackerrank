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
    for i in range(n):
        # print('i', i)
        if q[i] > (i+1):
            # print('q[i]', q[i])
            # print('i+1', i+1)
            if q[i] == (i+2):
                count += 1
                # print('count if-1', count)
                continue
            elif q[i] == (i+3):
                count += 2
                # print('count elif-1', count)
                continue
            else:
                flag = False

        # elif q[i] < (i+1):
        #     print('q[i]', q[i])
        #     print('i+1', i+1)
        #     if q[i] == i:
        #         count += 1
        #         print('count if-2', count)
        #         continue
        #     elif q[i] == (i-1):
        #         count += 1
        #         print('count elif-2', count)
        #         continue
        else:
            continue

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
