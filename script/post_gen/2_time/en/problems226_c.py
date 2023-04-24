Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], dp[i] + T[i])
        for j in A[i]:
            dp[i + 1] = min(dp[i + 1], dp[j] + T[i])
    print(dp[N])

=======
Suggestion 2

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [float("inf")] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for j in range(K[i]):
            dp[i] = min(dp[i], dp[A[i][j] - 1] + T[i])
    print(dp[N - 1])

=======
Suggestion 3

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())

    dp = [float('inf')] * N
    dp[0] = T[0]
    for i in range(N):
        dp[i] = min(dp[i], dp[i-1] + T[i])
        for j in range(K[i]):
            dp[A[i][j]-1] = min(dp[A[i][j]-1], dp[i])

    print(dp[N-1])

=======
Suggestion 4

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [float('inf')] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min([dp[j - 1] + T[i] for j in A[i]])
    print(dp[N - 1])

=======
Suggestion 5

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for i in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        dp[i] = 10 ** 18
        for j in range(K[i]):
            dp[i] = min(dp[i], dp[A[i][j] - 1] + T[i])
    print(dp[0])

=======
Suggestion 6

def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = t[i] + max(dp[j - 1] for j in a[i])
    print(dp[n - 1])

=======
Suggestion 7

def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        A.append(a)
    dp = [float('inf')] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for a in A[i]:
            dp[i] = min(dp[i], dp[a - 1] + T[i])
    print(dp[N - 1])

=======
Suggestion 8

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[]] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = T[0]
    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i] + T[i+1])
        for j in range(K[i]):
            dp[A[i][j] - 1] = min(dp[A[i][j] - 1], dp[i] + T[A[i][j] - 1])
    print(dp[N-1])

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    for i in range(N):
        T, K = map(int, input().split())
        a = list(map(int, input().split()))
        A.append((T, K, a))
    dp = [0] * N
    dp[0] = A[0][0]
    for i in range(1, N):
        dp[i] = dp[i-1] + A[i][0]
        for j in range(A[i][1]):
            dp[i] = min(dp[i], dp[A[i][2][j]-1] + A[i][0])
    print(dp[N-1])

=======
Suggestion 10

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    n = int(input())
    t = [0]*n
    k = [0]*n
    a = [0]*n
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())
    dp = [0]*n
    dp[0] = t[0]
    for i in range(1, n):
        dp[i] = t[i] + dp[i-1]
        for j in range(k[i]):
            dp[i] = min(dp[i], dp[a[i][j]-1] + t[i])
    print(dp[n-1])
