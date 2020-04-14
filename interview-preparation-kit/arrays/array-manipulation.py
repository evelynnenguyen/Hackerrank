#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l = [0] * n
    lq = len(queries)

    #O(nm)
    # for i in range(lq):
    #     for j in range(queries[i][0]-1, queries[i][1]):
    #         l[j] += queries[i][2]
    # result = max(l)
    # return result

    #O(m+n)
    # for i in range(lq):
    #     l[queries[i][0]-1] += queries[i][2]
    #     if queries[i][1] < n:
    #         l[queries[i][1]] -= queries[i][2]
    #     print(l)
    # for j in range(1,n):
    #     l[j] += l[j-1]

    #O(m+n)
    # for i in range(lq):
    #     l[queries[i][0]-1] += queries[i][2]
    #     if queries[i][1] < n:
    #         l[queries[i][1]] -= queries[i][2]
    #     print(l)
    # for j in range(1,n):
    #     l[j] += l[j-1]
    result = max(l)
    return result

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        queries = []
        for _ in range(m):
            queries.append(list(map(int, input().rstrip().split())))
        result = arrayManipulation(n, queries)
        print(result)
