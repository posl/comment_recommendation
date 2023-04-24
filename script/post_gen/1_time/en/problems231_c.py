Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        j = 0
        while j < n and a[j] < x[i]:
            j += 1
        print(n - j)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x = int(input())
        cnt = 0
        for a in A:
            if a >= x:
                cnt += 1
        print(cnt)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        import bisect
        print(N-bisect.bisect_left(A, x))

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        idx = bisect.bisect_left(a, i)
        print(n-idx)

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(q):
        x = int(input())
        index = binary_search(a, x)
        print(n - index)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    for i in range(Q):
        x = int(input())
        count = 0
        for j in range(N):
            if A[j] >= x:
                count += 1
        print(count)

=======
Suggestion 8

def main():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        idx = bisect.bisect_left(a,x[i])
        print(n-idx)

=======
Suggestion 9

def solve(n, q, a, x):
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
x = []
for i in range(q):
    x.append(int(input()))
solve(n, q, a, x)
