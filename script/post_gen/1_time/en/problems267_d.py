Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, s[i + m] - s[i] + m * max(a[i:i + m]))
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        for j in range(i + M, N + 1):
            ans = max(ans, sum(range(M + 1)) * sum(A[i:j]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(M):
        ans += (i+1) * A[i]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            if i+j < N:
                sum += (j+1) * A[i+j]
        ans = max(ans, sum)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, M+1):
        ans += i * max(A)
        A.remove(max(A))
    print(ans)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    from heapq import heapify, heappop, heappush
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (A[i], i)
    B.sort()
    heapify(B)
    C = [0] * N
    for i in range(N):
        C[i] = (A[i], i)
    C.sort(reverse=True)
    heapify(C)
    ans = 0
    for i in range(1, M + 1):
        a, b = heappop(B)
        c, d = heappop(C)
        if a >= c:
            ans += a * i
            heappush(B, (a, b))
        else:
            ans += c * i
            heappush(C, (c, d))
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N+1):
        A[i] += A[i-1]
    for i in range(N-M+1):
        ans = max(ans, A[i+M] - A[i])
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    b = [a[i] - a[i - 1] for i in range(1, n)]
    b = sorted(b, reverse=True)
    print(sum(a[m - 1:]) - sum(b[:m - 1]))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
        for j in range(i):
            b[i] = max(b[i],b[j] + a[i-j-1])
    print(max(b))

=======
Suggestion 10

def main():
    from sys import stdin
    from math import ceil
    readline = stdin.readline

    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))

    B = sorted([a - i for i, a in enumerate(A, 1)], reverse=True)
    ans = 0
    for i in range(M):
        ans += ceil(B[i] / M)

    print(ans)
