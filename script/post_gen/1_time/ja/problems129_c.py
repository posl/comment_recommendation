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
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    print(dp[N])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for _ in range(m):
        a[int(input())] = 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if a[i] == 0:
            dp[i + 1] += dp[i]
            dp[i + 1] %= 1000000007
            if i + 2 <= n:
                dp[i + 2] += dp[i]
                dp[i + 2] %= 1000000007
    print(dp[n])

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = [int(input()) for _ in range(M)]
    mod = 10**9 + 7
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    for i in range(1,N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] + [int(input()) for _ in range(M)] + [N+1]
    A.sort()
    MOD = 10**9 + 7

    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD
    print(dp[N])

=======
Suggestion 5

def main():
    #入力
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]

    #初期化
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1

    #壊れている床を踏まないようにしながら、最上段(N 段目)にたどりつくまでの移動方法は何通りあるでしょうか？
    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    a = [0] + a + [n+1]
    a.sort()
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % (10**9+7)
    print(dp[n])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A = [0]+A
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N):
        if i+1 in A:
            continue
        if i+2 in A:
            dp[i+1] = dp[i]
        else:
            dp[i+1] = dp[i]+dp[i-1]
    print(dp[N]%(10**9+7))

=======
Suggestion 8

def main():
    N, M = [int(i) for i in input().split()]
    A = [int(input()) for i in range(M)]
    A.append(0)
    A.append(N+1)
    A.sort()
    A = [A[i+1]-A[i]-1 for i in range(M+1)]
    dp = [0]*(M+2)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, M+2):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    ans = 1
    for i in range(M+1):
        ans *= dp[A[i]]
        ans %= 1000000007
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N)
    a.append(0)
    a.sort()
    a.reverse()
    mod = 10 ** 9 + 7

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if i + 1 in a:
            continue
        dp[i + 1] = dp[i] + dp[i - 1]
        dp[i + 1] %= mod
    print(dp[N])

=======
Suggestion 10

def main():
    # データの入力
    N,M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # DPテーブルの初期化
    dp = [0] * (N+2)
    dp[0] = 1
    # 壊れている床を1、壊れていない床を0とする
    broken = [0] * (N+2)
    for a in A:
        broken[a] = 1
    # DPループ
    for i in range(N+1):
        if broken[i] == 1:
            continue
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
        dp[i+1] %= 1000000007
        dp[i+2] %= 1000000007
    # 答えの出力
    print(dp[N])
