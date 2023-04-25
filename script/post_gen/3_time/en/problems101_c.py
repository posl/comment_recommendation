Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if N % K == 0:
        ans = 0
    else:
        ans = 1
    ans += N // K
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = dp[i] + A[i]
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, dp[i + K] - dp[i])
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(0, n, k):
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    import sys
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    #dp[i][j]: i番目の要素までで、j個のグループに分割する時の最小値
    dp = [[10**9]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N+1):
            if dp[i][j] == 10**9:
                continue
            for k in range(K+1):
                if i+k > N:
                    break
                dp[i+k][j+1] = min(dp[i+k][j+1], max(dp[i][j], A[i+k-1]))
    ans = 10**9
    for i in range(N+1):
        ans = min(ans, dp[N][i])
    print(ans)

=======
Suggestion 5

def solve(n, k, a):
    a = a[::-1]
    count = 0
    for i in range(n):
        if a[i] == i + 1:
            count += 1
            i += k - 1
    return (n + k - 1) // k - (count + k - 1) // k

=======
Suggestion 6

def main():
    #input
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    #calc
    ans = 0
    while max(A) > min(A) + K:
        ans += 1
        for i in range(N):
            if A[i] == max(A):
                for j in range(K):
                    if i+j < N:
                        A[i+j] = max(A)

    #output
    print(ans)

=======
Suggestion 7

def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    #compute
    #AをK個ずつに分けて、それぞれの最小値の数を数える
    #最小値の数が最小になるように、Aを分割する
    #最小値の数が最小になるようにするには、AをK個ずつに分けて、
    #最小値の数を数えるときに、K-1個ずつの数を数える
    #最小値の数が最小になるようにするには、AをK-1個ずつに分ける
    #最小値の数が最小になるようにするには、AをK-1個ずつに分けて、
    #最小値の数を数えるときに、K-2個ずつの数を数える
    #最小値の数が最小になるようにするには、AをK-2個ずつに分ける
    #最小値の数が最小になるようにするには、AをK-2個ずつに分けて、
    #最小値の数を数えるときに、K-3個ずつの数を数える
    #最小値の数が最小になるようにするには、AをK-3個ずつに分ける
    #最小値の数が最小になるようにするには、AをK-3個ずつに分けて、
    #最小値の数を数えるときに、K-4個ずつの数を数える
    #最小値の数が最小になるようにするには、AをK-4個ずつに分

=======
Suggestion 8

def solve(N, K, A):
    # N: length of the sequence
    # K: number of consecutive elements to be replaced
    # A: the sequence
    # return: the minimum number of operations required
    if N == K:
        return 1
    if K % 2 == 0:
        for i in range(N):
            if A[i] != i + 1:
                return (N - 1) // (K // 2) + 1
        return 1
    else:
        for i in range(N):
            if A[i] != N - i:
                return (N - 1) // (K // 2) + 1
        return 1
