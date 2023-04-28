Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        q = input().split()
        if q[0] == '1':
            s.append(int(q[1]))
        elif q[0] == '2':
            x = int(q[1])
            c = int(q[2])
            for i in range(c):
                if x in s:
                    s.remove(x)
        elif q[0] == '3':
            print(max(s) - min(s))

=======
Suggestion 2

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            S.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            for j in range(min(c, S.count(x))):
                S.remove(x)
        else:
            print(max(S)-min(S))

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s) - min(s))

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        line = input().split()
        if line[0] == '1':
            S.append(int(line[1]))
        elif line[0] == '2':
            x = int(line[1])
            c = int(line[2])
            for j in range(c):
                if x in S:
                    S.remove(x)
                else:
                    break
        elif line[0] == '3':
            print(max(S)-min(S))

=======
Suggestion 5

def main():
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    s = []
    for q in queries:
        if q[0] == 1:
            s.append(q[1])
        elif q[0] == 2:
            for _ in range(min(q[2], s.count(q[1]))):
                s.remove(q[1])
        else:
            print(max(s) - min(s))
    return

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    max_s = 0
    min_s = 0
    for _ in range(n):
        q = input().split()
        if q[0] == '1':
            s.append(int(q[1]))
            if len(s) == 1:
                max_s = s[0]
                min_s = s[0]
            else:
                if max_s < s[-1]:
                    max_s = s[-1]
                if min_s > s[-1]:
                    min_s = s[-1]
        elif q[0] == '2':
            c = int(q[2])
            for _ in range(min(c, s.count(int(q[1])))):
                s.remove(int(q[1]))
            if len(s) == 0:
                max_s = 0
                min_s = 0
            else:
                max_s = max(s)
                min_s = min(s)
        else:
            print(max_s - min_s)

=======
Suggestion 7

def main():
    # input
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    # compute
    S = []
    ans = []
    for query in queries:
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            num = int(query[1])
            c = min(int(query[2]), S.count(num))
            for _ in range(c):
                S.remove(num)
        else:
            ans.append(max(S) - min(S))
    # output
    for s in ans:
        print(s)

=======
Suggestion 8

def main():
    from sys import stdin
    from collections import defaultdict
    from heapq import heappush, heappop
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    from math import ceil, floor, sqrt, gcd
    from copy import deepcopy
    from decimal import Decimal
    from functools import reduce
    from fractions import Fraction
    from random import randint
    from string import ascii_lowercase, ascii_uppercase, digits
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    from heapq import heappush, heappop
    from collections import defaultdict
    from copy import deepcopy
    from math import ceil, floor, sqrt, gcd
    from decimal import Decimal
    from fractions import Fraction
    from random import randint
    from string import ascii_lowercase, ascii_uppercase, digits
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    from heapq import heappush, heappop
    from collections import defaultdict
    from copy import deepcopy
    from math import ceil, floor, sqrt, gcd
    from decimal import Decimal
    from fractions import Fraction
    from random import randint
    from string import ascii_lowercase, ascii_uppercase, digits
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    from heapq import heappush, heappop
    from collections import defaultdict
    from copy import deepcopy
    from math import ceil, floor, sqrt, gcd
    from decimal import Decimal
    from fractions import Fraction
    from random import randint
    from string import ascii_lowercase, ascii_uppercase, digits
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    from heapq import heappush, heappop
    from collections import defaultdict
    from copy import deepcopy
    from math import ceil, floor, sqrt, gcd
    from decimal import Decimal
    from fractions import Fraction
    from random import randint
    from string import ascii_lowercase, ascii_uppercase, digits
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from

=======
Suggestion 9

def main():
    from sys import stdin
    input = stdin.readline
    from collections import defaultdict
    import heapq

    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    s = []
    d = defaultdict(int)

    for query in queries:
        if query[0] == 1:
            heapq.heappush(s, query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            while query[2] > 0 and s:
                if d[s[0]] >= query[2]:
                    d[s[0]] -= query[2]
                    query[2] = 0
                else:
                    query[2] -= d[s[0]]
                    d[s[0]] = 0
                    heapq.heappop(s)
        else:
            print(max(s) - min(s))

=======
Suggestion 10

def main():
    from collections import Counter
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline
    q = int(input())
    s = []
    s_c = Counter()
    s_max = []
    s_min = []
    s_sum = 0
    for _ in range(q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            s.append(q[1])
            heappush(s_max, -q[1])
            heappush(s_min, q[1])
            s_sum += q[1]
            s_c[q[1]] += 1
        elif q[0] == 2:
            while q[2] > 0 and s_c[q[1]] > 0:
                s_c[q[1]] -= 1
                q[2] -= 1
                s_sum -= q[1]
            while s_max and s_c[-s_max[0]] == 0:
                heappop(s_max)
            while s_min and s_c[s_min[0]] == 0:
                heappop(s_min)
        else:
            print(-s_max[0] - s_min[0])
    return
