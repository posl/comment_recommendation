Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            x, c = int(query[1]), int(query[2])
            for j in range(min(c, S.count(x))):
                S.remove(x)
        else:
            print(max(S) - min(S))

=======
Suggestion 2

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    q = int(input())
    s = Counter()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s[query[1]] += 1
        elif query[0] == 2:
            c = min(query[2], s[query[1]])
            s[query[1]] -= c
            if s[query[1]] == 0:
                del s[query[1]]
        else:
            print(max(s.keys()) - min(s.keys()))

=======
Suggestion 3

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

=======
Suggestion 4

def main():
  # N = int(input())
  # A = list(map(int, input().split()))
  # A, B, C = map(int, input().split())
  # S = input()
  # N, K = map(int, input().split())
  # S = input()
  # A = list(map(int, input().split()))
  # A = [list(map(int, input().split())) for _ in range(N)]
  Q = int(input())
  # Q = N
  # A = list(map(int, input().split()))
  # A = [list(map(int, input().split())) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]
  # A = [int(input()) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]

  # N = int(input())
  # A = list(map(int, input().split()))
  # A, B, C = map(int, input().split())
  # S = input()
  # N, K = map(int, input().split())
  # S = input()
  # A = list(map(int, input().split()))
  # A = [list(map(int, input().split())) for _ in range(N)]
  # Q = int(input())
  # A = [list(map(int, input().split())) for _ in range(N)]
  # A = [int(input()) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]


  # A = [int(input()) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]

  # A = [int(input()) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]
  # A = [list(map(int, input().split())) for _ in range(N)]
  # B = [list(map(int, input().split())) for _ in range(N)]
  # A = [int(input()) for _ in range(N)]
  # B = [int(input

=======
Suggestion 5

def solve():
    from sys import stdin
    from collections import Counter
    from heapq import heappush, heappop
    input = stdin.readline
    q = int(input())
    s = Counter()
    minheap = []
    maxheap = []
    for _ in range(q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            s[query[1]] += 1
            heappush(minheap, query[1])
            heappush(maxheap, -query[1])
        elif query[0] == 2:
            while s and query[2]:
                if s[minheap[0]] <= query[2]:
                    query[2] -= s[minheap[0]]
                    s.pop(minheap[0])
                    heappop(minheap)
                else:
                    s[minheap[0]] -= query[2]
                    query[2] = 0
        else:
            while s and s[minheap[0]] == 0:
                s.pop(minheap[0])
                heappop(minheap)
            while s and s[-maxheap[0]] == 0:
                s.pop(-maxheap[0])
                heappop(maxheap)
            print(-maxheap[0] - minheap[0])

=======
Suggestion 6

def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = defaultdict(int)
    max_s = 0
    min_s = 10**9
    for _ in range(N):
        q = input().split()
        if q[0] == '1':
            S[q[1]] += 1
            max_s = max(max_s, int(q[1]))
            min_s = min(min_s, int(q[1]))
        elif q[0] == '2':
            n = S[q[1]]
            if n <= int(q[2]):
                S[q[1]] = 0
            else:
                S[q[1]] -= int(q[2])
            if S[q[1]] == 0:
                del S[q[1]]
        else:
            print(max_s - min_s)

=======
Suggestion 7

def main():
    from sys import stdin
    from collections import Counter
    from heapq import heappop, heappush
    input = stdin.buffer.readline
    N = int(input())
    S = []
    Smin = []
    Smax = []
    Ssum = 0
    Ssum_min = 0
    Ssum_max = 0
    count = Counter()
    for _ in range(N):
        query = input().split()
        if query[0] == b'1':
            x = int(query[1])
            Ssum += x
            heappush(S, x)
            count[x] += 1
            if len(Smin) == 0 or x <= Smin[0]:
                heappush(Smin, x)
                Ssum_min += x
            else:
                heappush(Smax, -x)
                Ssum_max += x
        elif query[0] == b'2':
            x = int(query[1])
            c = int(query[2])
            while c > 0:
                if count[x] == 0:
                    break
                if x <= Smin[0]:
                    heappop(Smin)
                    Ssum_min -= x
                else:
                    heappop(Smax)
                    Ssum_max -= x
                heappop(S)
                Ssum -= x
                count[x] -= 1
                c -= 1
        else:
            print(-Smin[0] + Ssum - Ssum_min + Ssum_max)
    return

=======
Suggestion 8

def solve():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    from bisect import bisect_right, bisect_left
    from heapq import heappop, heappush
    import heapq

    Q = int(input())
    q = []
    q2 = []
    q3 = []
    d = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(q, query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            while query[1] > 0:
                if len(q) == 0:
                    break
                x = heappop(q)
                if d[x] > 1:
                    d[x] -= 1
                    heappush(q, x)
                else:
                    d[x] -= 1
                query[1] -= 1
        else:
            while len(q) > 0:
                x = heappop(q)
                if d[x] > 1:
                    d[x] -= 1
                    heappush(q, x)
                else:
                    d[x] -= 1
                    d2[x] += 1
                    heappush(q2, x)
                    d3[x] += 1
                    heappush(q3, -x)
                    break
            print(-q3[0] - q2[0])

=======
Suggestion 9

def main():
    # Get the number of queries
    Q = int(input())

    # Initialize the list
    S = []

    # Process the queries
    for i in range(Q):
        # Get the query
        query = input().split()

        # Process the query
        if query[0] == '1':
            # Get the integer
            x = int(query[1])

            # Add the integer to the list
            S.append(x)
        elif query[0] == '2':
            # Get the integer and the count
            x = int(query[1])
            c = int(query[2])

            # Remove the integer from the list c times
            for j in range(min(c, S.count(x))):
                S.remove(x)
        else:
            # Print the maximum value of the list minus the minimum value of the list
            print(max(S) - min(S))

=======
Suggestion 10

def get_min_max_diff(nums):
    return max(nums) - min(nums)
