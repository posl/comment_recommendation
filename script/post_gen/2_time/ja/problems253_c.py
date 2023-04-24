Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            if query[1] in S:
                for j in range(query[2]):
                    S.remove(query[1])
        else:
            print(max(S)-min(S))

=======
Suggestion 2

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    d = defaultdict(int)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d[query[1]] += 1
        elif query[0] == 2:
            if d[query[1]] != 0:
                d[query[1]] -= min(query[2], d[query[1]])
        else:
            print(max(d) - min(d))

=======
Suggestion 3

def main():
    import sys
    from heapq import heappush, heappop
    input = sys.stdin.readline
    Q = int(input())
    hq = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(hq, query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], hq.count(query[1]))):
                hq.remove(query[1])
        else:
            print(heappop(hq) - heappop(hq))
            heappush(hq, heappop(hq))
            heappush(hq, heappop(hq))

=======
Suggestion 4

def main():
    from collections import Counter
    import sys
    input = sys.stdin.buffer.readline
    Q = int(input())
    D = Counter()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            D[query[1]] += 1
        elif query[0] == 2:
            D[query[1]] -= min(query[2], D[query[1]])
            if D[query[1]] <= 0:
                del D[query[1]]
        else:
            print(max(D.keys()) - min(D.keys()))

=======
Suggestion 5

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    S = defaultdict(int)
    maxS = 0
    minS = 10**9
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S[query[1]] += 1
            maxS = max(maxS,query[1])
            minS = min(minS,query[1])
        elif query[0] == 2:
            S[query[1]] -= min(query[2],S[query[1]])
            if S[query[1]] == 0:
                del S[query[1]]
                if query[1] == maxS:
                    maxS = max(S.keys()) if len(S) > 0 else 0
                if query[1] == minS:
                    minS = min(S.keys()) if len(S) > 0 else 10**9
        else:
            print(maxS - minS)
    return

=======
Suggestion 6

def main():
    import sys
    from collections import Counter
    from heapq import heappop, heappush
    input = sys.stdin.readline
    Q = int(input())
    q = []
    for _ in range(Q):
        q.append(list(map(int, input().split())))
    counter = Counter()
    heap = []
    for _q in q:
        if _q[0] == 1:
            counter[_q[1]] += 1
            heappush(heap, _q[1])
        elif _q[0] == 2:
            if _q[1] in counter:
                if counter[_q[1]] <= _q[2]:
                    del counter[_q[1]]
                    while heap[0] != _q[1]:
                        heappop(heap)
                    heappop(heap)
                else:
                    counter[_q[1]] -= _q[2]
        else:
            print(heap[-1] - heap[0])

=======
Suggestion 7

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    #S は空
    S = Counter()
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S[query[1]] += 1
        elif query[0] == 2:
            S[query[1]] -= min(S[query[1]],query[2])
            if S[query[1]] == 0:
                del S[query[1]]
        else:
            print(max(S.keys())-min(S.keys()))

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict, deque
    Q = int(input())
    a = defaultdict(int)
    b = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]] += 1
            b.append(query[1])
        elif query[0] == 2:
            if a[query[1]] > 0:
                a[query[1]] -= 1
                b.append(query[1])
        else:
            while b:
                q = b.popleft()
                if a[q] > 0:
                    a[q] -= 1
                    print(q - b[0])
                    break

=======
Suggestion 9

def main():
    import sys
    #import collections
    #import heapq
    #import math
    #import re
    #import string
    #import itertools
    #import numpy as np
    #from collections import Counter
    #from collections import defaultdict
    #from decimal import Decimal
    #from functools import reduce
    #from itertools import combinations
    #from itertools import permutations
    #from itertools import product
    #from operator import itemgetter
    #from operator import mul
    #from operator import truediv
    #from operator import add
    #from operator import sub
    #from queue import Queue
    #from queue import LifoQueue
    #from queue import PriorityQueue
    #from scipy.misc import comb
    #from scipy.sparse.csgraph import floyd_warshall
    #from scipy.sparse.csgraph import dijkstra
    #from scipy.sparse.csgraph import bellman_ford
    #from scipy.sparse.csgraph import shortest_path
    #from scipy.sparse.csgraph import johnson
    #from scipy.sparse import csr_matrix
    #from scipy.sparse import lil_matrix
    #from scipy.sparse import dok_matrix
    #from scipy.sparse import dia_matrix
    #from scipy.sparse import csc_matrix
    #from scipy.sparse import coo_matrix
    #from scipy.sparse import bsr_matrix
    #from scipy.sparse import spdiags
    #from scipy.sparse import eye
    #from scipy.sparse import identity
    #from scipy.sparse import kron
    #from scipy.sparse import triu
    #from scipy.sparse import tril
    #from scipy.sparse import block_diag
    #from scipy.sparse.linalg import inv
    #from scipy.sparse.linalg import eigs
    #from scipy.sparse.linalg import eigsh
    #from scipy.sparse.linalg import svds
    #from scipy.sparse.linalg import lsqr
    #from scipy.sparse.linalg import spsolve
    #from scipy.sparse.linalg import spsolve_triangular
    #from scipy.sparse.linalg import expm
    #from scipy.sparse.linalg import expm_multiply
    #from scipy.sparse.linalg import expm_frechet
    #from scipy.sparse.linalg import logm
    #from scipy.sparse.linalg import sinm
    #from scipy.sparse.linalg import cosm
    #from scipy.sparse.linalg import tanm
    #from scipy.sparse.linalg import sinhm

=======
Suggestion 10

def  main():
     from  collections  import  defaultdict
