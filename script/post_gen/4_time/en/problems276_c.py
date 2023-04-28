Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(' '.join(map(str, Q)))

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i, v in enumerate(p):
        q[v - 1] = i + 1
    print(*q)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n

    for i in range(n):
        q[p[i]-1] = i+1

    print(" ".join(map(str, q)))

=======
Suggestion 5

def main():
    # Write code here
    n = int(input())
    p = list(map(int,input().split()))
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)

    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1

    print(*Q)

=======
Suggestion 7

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

=======
Suggestion 8

def get_lexicographically_smallest_permutation(N, P):
    sorted_P = sorted(P)
    sorted_P.reverse()
    sorted_P.append(0)
    sorted_P.reverse()
    return sorted_P

N = int(input())
P = list(map(int, input().split()))
print(" ".join(map(str, get_lexicographically_smallest_permutation(N, P))))
