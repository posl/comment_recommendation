Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_right(a, x[i]))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(N - bisect.bisect_left(A, x))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(bisect.bisect_right(A, x))

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()
    for i in range(q):
        l, r = 0, n
        while r - l > 1:
            c = (l + r) // 2
            if a[c] >= x[i]:
                r = c
            else:
                l = c
        print(n - r)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(len(A) - A.index(x) if x in A else len(A) - A.index(x) + 1)

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for i in range(q)]

    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 7

def main():
    #input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    #compute
    A.sort()
    for x in X:
        ans = 0
        for a in A:
            if a >= x:
                break
            ans += 1
        print(N - ans)

=======
Suggestion 8

def main():
    n, q, = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 9

def main():
    #input
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for _ in range(Q)]

    #sort
    A.sort()

    #cumulative sum
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]

    #binary search
    for i in range(Q):
        ok = 0
        ng = N+1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A[mid-1] >= x[i]:
                ng = mid
            else:
                ok = mid
        print(N-ng+1)
