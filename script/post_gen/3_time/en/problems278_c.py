Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,Q = map(int,input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int,input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    follow = []
    for i in range(N):
        follow.append([])
    for i in range(Q):
        if T[i] == 1:
            follow[A[i]-1].append(B[i])
        elif T[i] == 2:
            if B[i] in follow[A[i]-1]:
                follow[A[i]-1].remove(B[i])
        else:
            if B[i] in follow[A[i]-1] and A[i] in follow[B[i]-1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    follow = set()
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.add((a, b))
        elif t == 2:
            if (a, b) in follow:
                follow.remove((a, b))
        else:
            if (a, b) in follow and (b, a) in follow:
                print("Yes")
            else:
                print("No")
    return

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    follow = set()
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.add((a, b))
        elif t == 2:
            if (a, b) in follow:
                follow.remove((a, b))
        else:
            if (a, b) in follow and (b, a) in follow:
                print("Yes")
            else:
                print("No")

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    follow = set()
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow.add((A, B))
        elif T == 2:
            follow.discard((A, B))
        else:
            print('Yes' if (A, B) in follow and (B, A) in follow else 'No')

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    follow = [set() for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            if b-1 in follow[a-1]:
                follow[a-1].remove(b-1)
        else:
            if b-1 in follow[a-1] and a-1 in follow[b-1]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    t = []
    a = []
    b = []
    for i in range(q):
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    follow = []
    for i in range(n):
        follow.append([])
    for i in range(q):
        if t[i] == 1:
            follow[a[i] - 1].append(b[i])
        elif t[i] == 2:
            if b[i] in follow[a[i] - 1]:
                follow[a[i] - 1].remove(b[i])
        elif t[i] == 3:
            if a[i] in follow[b[i] - 1] and b[i] in follow[a[i] - 1]:
                print("Yes")
            else:
                print("No")

main()

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    following = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            following[A - 1].add(B - 1)
        elif T == 2:
            following[A - 1].discard(B - 1)
        else:
            if B - 1 in following[A - 1] and A - 1 in following[B - 1]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    follow = {}
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            if A not in follow:
                follow[A] = set()
            follow[A].add(B)
        elif T == 2:
            if A in follow:
                follow[A].discard(B)
        else:
            if A in follow and B in follow[A]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 9

def main():
    import sys
    import math
    import collections
    import bisect
    import heapq
    import time
    import random
    import itertools
    import numpy as np
    import scipy as sp
    import numba
    from numba import njit
    from numba import i8, u1, u4, u8, f8, b1
    from numba.types import Tuple
    from numba.experimental import jitclass
    from numba import types
    from numba.typed import Dict
    from numba.typed import List
    from numba import prange
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import dijkstra
    from collections import deque
    from collections import defaultdict
    from collections import Counter
    from collections import deque
    from collections import defaultdict
    from functools import lru_cache
    from itertools import permutations
    from itertools import combinations
    from itertools import combinations_with_replacement
    from itertools import product
    from itertools import accumulate
    from itertools import groupby
    from heapq import heappush, heappop, heapify
    from bisect import bisect_left, bisect_right, insort_left, insort_right
    from operator import itemgetter
    from operator import mul
    from operator import add
    from operator import sub
    from operator import truediv
    from operator import floordiv
    from functools import reduce
    from functools import lru_cache
    from functools import partial
    from functools import cmp_to_key
    from math import gcd
    from math import factorial
    from math import sqrt
    from math import ceil
    from math import floor
    from scipy.special import comb
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import dijkstra
    from scipy.sparse.csgraph import floyd_warshall
    from scipy.sparse.csgraph import bellman_ford
    from scipy.sparse.csgraph import johnson
    from scipy.sparse.csgraph import breadth_first_order
    from scipy.sparse.csgraph import depth_first_order
    from scipy.sparse.csgraph import breadth_first_tree
    from scipy.sparse.csgraph import depth_first_tree
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse.csgraph import laplacian
    from scipy.sparse.csgraph import maximum_bip

=======
Suggestion 10

def main():
    n, q = map(int, input().split())

    # 1-indexed
    # 0: not following
    # 1: following
    following = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            following[a][b] = 1
        elif t == 2:
            following[a][b] = 0
        else:
            if following[a][b] == 1:
                print("Yes")
            else:
                print("No")
