Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        if K[i] == 0:
            dp[i] = T[i]
        else:
            dp[i] = max(T[i] + dp[j] for j in A[i])
    print(dp[0])

=======
Suggestion 2

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))

    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = dp[i] + T[i]
        for j in range(K[i]):
            dp[i + 1] = min(dp[i + 1], dp[A[i][j]] + T[i])

    print(dp[N])

=======
Suggestion 3

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for i in range(N)]
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [float("inf")] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for j in A[i]:
            dp[i] = min(dp[i], dp[j - 1] + T[i])
    print(dp[-1])

=======
Suggestion 4

def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [0] * n
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = t[0]
    for i in range(1, n):
        dp[i] = dp[i-1] + t[i]
        for j in a[i]:
            dp[i] = min(dp[i], dp[j-1] + t[i])
    print(dp[n-1])

=======
Suggestion 5

def main():
    N = int(input())
    T = [0]*N
    K = [0]*N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [float('inf')]*N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i-1]+T[i])
        for a in A[i]:
            dp[i] = min(dp[i], dp[a-1]+T[i])
    print(dp[-1])

=======
Suggestion 6

def main():
    n = int(input())
    T = [0] * n
    K = [0] * n
    A = [[] for _ in range(n)]
    for i in range(n):
        t, k = map(int, input().split())
        T[i] = t
        K[i] = k
        a = list(map(int, input().split()))
        A[i] = a

    dp = [0] * n
    for i in range(n):
        dp[i] = T[i]
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j] - 1] + T[i])

    print(dp[n - 1])

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    # dp[i]: i番目の技を覚えるのにかかる最小時間
    dp = [10 ** 18] * N
    dp[0] = T[0]
    for i in range(N):
        dp[i] = min(dp[i], dp[i - 1] + T[i])
        for j in range(K[i]):
            dp[A[i][j] - 1] = min(dp[A[i][j] - 1], dp[i])
    print(dp[N - 1])

=======
Suggestion 8

def main():
    N = int(input())
    dp = [0]*(N+1)
    for i in range(N):
        T, K, *A = map(int, input().split())
        dp[i+1] = T + min(dp[j] for j in A)
    print(dp[-1])

=======
Suggestion 9

def main():
    # Get input
    N = int(input())
    T = []
    A = []
    for i in range(N):
        t, k = list(map(int, input().split()))
        T.append(t)
        A.append(list(map(lambda x: int(x)-1, input().split())))
    # Solve
    dp = [0] * N
    for i in range(1, N):
        dp[i] = T[i] + min([dp[j] for j in A[i]])
    print(dp[-1])

=======
Suggestion 10

def main():
    import sys
    from collections import deque

    def input(): return sys.stdin.readline().rstrip()

    N = int(input())
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K = map(int, input().split())
        A[i] = list(map(int, input().split()))

    G = [[] for _ in range(N)]
    for i in range(N):
        for j in A[i]:
            G[j-1].append(i)

    dp = [0] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = dp[i-1] + T[i]
        for j in G[i]:
            dp[i] = min(dp[i], dp[j-1] + T[i])

    print(dp[-1])
