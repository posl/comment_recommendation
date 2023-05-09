def solve():
    # import sys
    # import collections
    # import math
    # import bisect
    # import heapq
    # import time
    # import itertools
    # import copy
    # import queue
    # import decimal
    # import functools
    # import random
    # import statistics
    # import string
    # import re
    # import numpy as np
    # sys.setrecursionlimit(10**6)
    # INF = 10**9
    # MOD = 10**9 + 7
    # input = sys.stdin.readline
    # input = lambda: sys.stdin.readline().rstrip()
    # input = lambda: sys.stdin.readline().rstrip()
    # input = lambda: int(sys.stdin.readline().rstrip())
    # input = lambda: map(int, sys.stdin.readline().rstrip().split())
    # input = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
    
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)
