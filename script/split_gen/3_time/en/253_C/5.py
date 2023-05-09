def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    import itertools
    Q = int(input())
    A = []
    B = []
    C = []
    for _ in range(Q):
        q = list(map(int, input().strip().split()))
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            B.append([q[1], q[2]])
        else:
            C.append(q[0])
    A.sort()
    heapify(A)
    for b in B:
        for _ in range(min(b[1], len(A))):
            A.remove(b[0])
        heapify(A)
    for c in C:
        print(max(A)-min(A))
