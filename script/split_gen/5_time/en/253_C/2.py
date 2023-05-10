def main():
    import sys
    from collections import defaultdict
    from bisect import bisect_left, bisect_right
    from heapq import heappush, heappop, heapify
    from itertools import permutations, combinations, product, combinations_with_replacement
    from math import ceil, floor, sqrt, gcd
    from copy import deepcopy
    from operator import itemgetter
    from functools import reduce
    sys.setrecursionlimit(10 ** 7)
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    read = sys.stdin.readline
    #read = sys.stdin.buffer.read
    q = int(read())
    query = []
    for i in range(q):
        query.append(list(map(int, read().split())))
    s = []
    s_max = []
    s_min = []
    for i in range(q):
        if query[i][0] == 1:
            heappush(s, query[i][1])
            heappush(s_max, -query[i][1])
            heappush(s_min, query[i][1])
        elif query[i][0] == 2:
            x = query[i][1]
            c = query[i][2]
            for j in range(c):
                if s[0] == x:
                    heappop(s)
                else:
                    break
            for j in range(c):
                if s_max[0] == -x:
                    heappop(s_max)
                else:
                    break
            for j in range(c):
                if s_min[0] == x:
                    heappop(s_min)
                else:
                    break
        else:
            print(-s_max[0]-s_min[0])
