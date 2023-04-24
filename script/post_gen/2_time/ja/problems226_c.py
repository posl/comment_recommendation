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
    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(N):
        dp[i] = min(dp[i], dp[i - 1] + T[i - 1])
        for j in range(K[i]):
            dp[A[i][j] - 1] = min(dp[A[i][j] - 1], dp[i] + T[i])
    print(dp[-1])

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
    # print(T)
    # print(K)
    # print(A)

    # dp[i] = 技 i を覚えるのにかかる最小時間
    dp = [0] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[j - 1] + T[i] for j in A[i])
    print(dp[-1])

=======
Suggestion 3

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * N
    for i in range(N):
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j] - 1])
        dp[i] += T[i]
    print(dp[-1])

=======
Suggestion 4

def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + T[i]
        for j in A[i]:
            dp[i] = min(dp[i], dp[j] + T[i])
    print(dp[N])

=======
Suggestion 5

def main():
    N = int(input())
    T = [0] * (N+1)
    K = [0] * (N+1)
    A = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = max(dp[j] for j in A[i]) + T[i]
    print(dp[N])

=======
Suggestion 6

def main():
    N = int(input())
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K = map(int, input().split())
        A[i] = list(map(int, input().split()))
    #print(N)
    #print(T)
    #print(A)
    #print('-----')

    # dp[i] : i 番目の技を覚えるのに必要な最小時間
    dp = [0] * N
    for i in range(N):
        #print('i = ', i)
        if i == 0:
            dp[i] = T[i]
            #print('dp[i] = ', dp[i])
            continue
        # A[i] に含まれる技をすべて覚えてから i 番目の技を覚える
        dp[i] = min(dp[j - 1] for j in A[i]) + T[i]
        #print('dp[i] = ', dp[i])
    print(dp[-1])

=======
Suggestion 7

def main():
    N = int(input())
    T = [0]
    K = [0]
    A = [[]]
    for i in range(N):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
        A.append(list(map(int, input().split())))
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + T[i]
        for j in A[i]:
            dp[i] = min(dp[i], dp[j] + T[i])
    print(dp[N])

=======
Suggestion 8

def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())

    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = max(dp[j - 1] for j in a[i]) + t[i]
    print(dp[n - 1])

=======
Suggestion 9

def main():
    N = int(input())
    T = [0] * (N+1)
    K = [0] * (N+1)
    A = [[0] for _ in range(N+1)]
    for i in range(1, N+1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = T[i] + max(dp[j] for j in A[i])
    print(dp[-1])

=======
Suggestion 10

def main():
    N = int(input())
    T = [0] + [int(input().split()[0]) for _ in range(N)]
    A = [list(map(int, input().split()[1:])) for _ in range(N)]
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = T[i] + max(dp[j] for j in A[i - 1])
    print(dp[-1])
