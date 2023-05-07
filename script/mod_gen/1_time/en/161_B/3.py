def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #N, M = 12, 3
    #A = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print("Yes")
    else:
        print("No")
main()
import sys
import math
import itertools
import collections
import heapq
import operator
import functools
import copy
import bisect
import string
import re
import random

if __name__ == '__main__':
    main()