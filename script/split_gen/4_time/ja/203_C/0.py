def main():
    # -*- coding: utf-8 -*-
    # 整数の入力
    import sys
    import math
    import numpy as np
    import bisect
    import copy
    import collections
    import itertools
    import heapq
    import decimal
    import fractions
    import statistics
    import queue
    import random
    import time
    import re
    import string
    import scipy.misc
    import scipy.special
    import functools
    import operator
    sys.setrecursionlimit(1000000)
    # 入力
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    #print(N, K)
    # 処理
    # 二分探索
    left = -1
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        #print(mid)
        #print(left, right)
        #print()
        #print(mid)
        #print()
        #print()
        #print()
