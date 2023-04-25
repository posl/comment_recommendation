Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    s = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        else:
            print(max(s)-min(s))

main()

=======
Suggestion 2

def main():
    q = int(input())
    s = []
    for i in range(q):
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
Suggestion 3

def main():
    n = int(input())
    a = []
    for _ in range(n):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a.append(q[1])
        elif q[0] == 2:
            for _ in range(min(q[2], a.count(q[1]))):
                a.remove(q[1])
        else:
            print(max(a) - min(a))

=======
Suggestion 4

def main():
    n = int(input())
    q = [input().split() for _ in range(n)]
    s = []
    for i in range(n):
        if q[i][0] == '1':
            s.append(int(q[i][1]))
        elif q[i][0] == '2':
            x = int(q[i][1])
            c = int(q[i][2])
            for j in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        elif q[i][0] == '3':
            print(max(s) - min(s))

=======
Suggestion 5

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += b[i] - a[i] + 1
    print(ans)

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(arr)
    for i in range(n):
        if arr[i][0] == 1:
            arr.append(arr[i][1])
        elif arr[i][0] == 2:
            if arr[i][1] in arr:
                arr.remove(arr[i][1])
        elif arr[i][0] == 3:
            print(max(arr)-min(arr))

=======
Suggestion 8

def main():
    from collections import Counter
    import heapq
    
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append([int(i) for i in input().split()])
    
    S = []
    heapq.heapify(S)
    counter = Counter()
    for query in queries:
        if query[0] == 1:
            heapq.heappush(S, query[1])
            counter[query[1]] += 1
        elif query[0] == 2:
            while query[2] > 0 and S:
                if counter[S[0]] <= query[2]:
                    query[2] -= counter[S[0]]
                    counter[S[0]] = 0
                    heapq.heappop(S)
                else:
                    counter[S[0]] -= query[2]
                    query[2] = 0
        else:
            print(max(S) - min(S))

=======
Suggestion 9

def main():
    # input
    Q = int(input())
    query = [input().split() for _ in range(Q)]

    # compute
    from collections import defaultdict
    d = defaultdict(int)
    min_val = 10**9
    max_val = 0

    for q in query:
        if q[0] == '1':
            x = int(q[1])
            d[x] += 1
            if x < min_val:
                min_val = x
            if x > max_val:
                max_val = x
        elif q[0] == '2':
            x = int(q[1])
            c = int(q[2])
            if d[x] > 0:
                if d[x] <= c:
                    d[x] = 0
                else:
                    d[x] -= c
        else:
            print(max_val-min_val)

=======
Suggestion 10

def problem253_c():
    pass
