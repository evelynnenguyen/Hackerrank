#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mapM = Counter(magazine)
    mapN = Counter(note)
    a = mapN - mapM
    if a == {}:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        magazine = input().rstrip().split()

        note = input().rstrip().split()

        checkMagazine(magazine, note)
