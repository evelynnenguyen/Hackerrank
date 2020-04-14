#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    result = (-9) * 7
    y = len(arr)
    x = len(arr[0])
    if x < 2 or y < 2:
        return (-9) * 7
    for i in range(x-2):
        for j in range(y-2):
            temp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            print(temp)
            if temp > result:
                result = temp
    return result

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    result = hourglassSum(arr)
    print('result', result)
