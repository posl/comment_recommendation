Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if i + 1 not in A:
            dp[i + 1] += dp[i]
        if i + 2 not in A:
            dp[i + 2] += dp[i]
        dp[i + 1] %= MOD
        dp[i + 2] %= MOD
    print(dp[-1])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]+dp[i-2]
    print(dp[N]%1000000007)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(0)
    A.append(N+1)
    A.sort()
    MOD = 10**9+7
    dp = [0]*(N+2)
    dp[0] = 1
    for i in range(1, N+2):
        if A[0] == i:
            A.pop(0)
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD

    print(dp[-1])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [int(input()) for i in range(M)]

    mod = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= mod
    print(dp[N])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    a.append(0)
    a.append(n+1)
    a.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[n])

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(0)
    A.append(N+1)
    A.sort()
    dp = [0]*(N+1)
    dp[0] = 1
    MOD = 10**9+7
    for i in range(1, N+1):
        if i not in A:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[N])

=======
Suggestion 7

def main():
    import sys
    from collections import defaultdict
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M = map(int, readline().split())
    A = list(map(int, read().split()))
    A.append(N)
    A.append(0)
    A.sort()
    #print(A)
    #print(N,M)
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[-1])
    return

=======
Suggestion 8

def main():
    # 入力
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # 答えを格納する変数
    ans = 0
    # 処理
    # 0段目から順に移動可能な場合の数を格納する配列
    dp = [0] * N
    # 0段目から移動可能な場合の数は1通り
    dp[0] = 1
    # 1段目から順に移動可能な場合の数を計算
    for i in range(1, N):
        # 1段目の場合
        if i == 1:
            # 壊れている床がある場合
            if i in A:
                dp[i] = 0
            # 壊れている床がない場合
            else:
                dp[i] = dp[i-1]
        # 2段目以降の場合
        else:
            # 壊れている床がある場合
            if i in A:
                dp[i] = 0
            # 壊れている床がない場合
            else:
                # 1段前と2段前の移動可能な場合の数の和
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    # 答え
    ans = dp[N-1]
    # 出力
    print(ans)

=======
Suggestion 9

def main():
    # 入力
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # 配列の初期化
    dp = [0] * (N + 1)
    # dp[0]の初期化
    dp[0] = 1
    # dp[i]の計算
    for i in range(1, N + 1):
        # 壊れている床の場合は0通り
        if i in A:
            dp[i] = 0
        # そうでない場合は、1段上がる場合と2段上がる場合の和
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    # 出力
    print(dp[N] % 1000000007)

=======
Suggestion 10

def main():
    # 入力
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]

    # 1,000,000,007 で割った余りを出力することに注意して下さい。
    MOD = 10**9 + 7

    # 解答
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % MOD)
