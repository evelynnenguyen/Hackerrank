#!/bin/python3
import timeit
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, q):
    # l = [0] * n
    # lq = len(q)

    #O(nm)
    # for i in range(lq):
    #     for j in range(queries[i][0]-1, queries[i][1]):
    #         l[j] += queries[i][2]
    # result = max(l)
    # return result

    #O(m+n)
    # for i in range(lq):
    #     l[q[i][0]-1] += q[i][2]
    #     if q[i][1] < n:
    #         l[q[i][1]] -= q[i][2]
    #     # print(l)
    # for j in range(1,n):
    #     l[j] += l[j-1]
    # r = max(l)
    # return r

    #O(m+n)
    l = [0] * (n+2)
    lq = len(q)
    for i in range(lq):
        l[q[i][0]] += q[i][2]
        l[q[i][1]+1] -= q[i][2]
    r = 0
    for j in range(1,n+2):
        l[j] += l[j-1]
        if l[j] > r:
            r = l[j]
    # r = max(l[1:n+1])
    return r

if __name__ == '__main__':
    # k = int(input())
    # for i in range(k):
    start = timeit.timeit()
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    q = []
    for _ in range(m):
        q.append(list(map(int, input().rstrip().split())))
    r = arrayManipulation(n, q)
    print(str(r))
    end = timeit.timeit()
    print(end - start)
