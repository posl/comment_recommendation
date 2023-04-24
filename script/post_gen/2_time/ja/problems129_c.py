Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in A:
            continue
        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    print(dp[N])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    broken = [False] * (N + 1)
    for i in range(M):
        broken[int(input())] = True
    dp = [0] * (N + 2)
    dp[0] = 1
    for i in range(1, N + 1):
        if not broken[i]:
            dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N] % 1000000007)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9 + 7

    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD

    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in a:
            continue
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 10 ** 9 + 7

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= mod
    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in a:
            dp[i] = 0
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % mod
    print(dp[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(int(input()))
    A.append(N+1)
    A.append(0)
    A.sort()
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    #初期化
    mod = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    #計算
    for i in range(1, N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]+dp[i-2]
            dp[i] %= mod
    #出力
    print(dp[N])

=======
Suggestion 9

def calc(N, M, A):
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD
    return dp[N]

=======
Suggestion 10

def main():
    #入力
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]
    #dp[i] = i段目にたどり着く方法の総数
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        #壊れている床を踏んでいないか
        if i not in A:
            #1段上がるか2段上がるか
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= 1000000007
    print(dp[N])
