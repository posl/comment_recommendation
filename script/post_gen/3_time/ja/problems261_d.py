Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    #dp[i][j]: i回目までのコイントスでj回連続表が出た時の最大金額
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        #i回目までのコイントスでj回連続表が出た時の最大金額
        for j in range(N + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            #表が出た時
            if X[i] == 1:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
                for k in range(M):
                    if j + 1 == C[k]:
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i] + Y[k])
            #裏が出た時
            else:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
    ans = 0
    for i in range(N + 1):
        ans = max(ans, dp[N][i])
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
            if j + 1 >= C[0]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1 - C[0]] + Y[0])
        for j in range(1, M):
            for k in range(N):
                if k + 1 >= C[j]:
                    dp[i + 1][k + 1] = max(dp[i + 1][k + 1], dp[i][k + 1 - C[j]] + Y[j])
    print(max(dp[N]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + Y[j])
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N+1)
    bonus = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + X[i-1]
        bonus[i] = bonus[i-1]
        for j in range(M):
            if i >= C[j]:
                bonus[i] = max(bonus[i], bonus[i-C[j]] + Y[j])
        dp[i] = max(dp[i], dp[i-1], dp[i] + bonus[i])
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    # dp[i] := i回目のコイントスで得られる最大の金額
    dp = [0] * (N + 1)
    # 連続ボーナスの最大値
    bonus = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
        for j in range(M):
            if i >= C[j]:
                bonus[i] = max(bonus[i], bonus[i - C[j]] + Y[j])
        dp[i] = max(dp[i], dp[i - 1] + bonus[i])
    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [0] * (N+1)
    dp[0] = X[0]
    for i in range(1, N):
        dp[i] = dp[i-1] + X[i]
        for j in range(M):
            if i + 1 - C[j] >= 0:
                dp[i] = max(dp[i], dp[i-C[j]] + Y[j])
    print(dp[N-1])

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i] + x[i])
        for j in range(m):
            if i + 1 >= c[j]:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - c[j]] + y[j])
    print(dp[n])

=======
Suggestion 8

def main():
    N, M = map(int,input().split())
    X = list(map(int,input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        ans += X[i]
        for j in range(M):
            if i + 1 == C[j]:
                ans += Y[j]
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(M)]
    B.sort(key=lambda x: -x[1])
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if B[j][0] <= i + 1:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - B[j][0]] + B[j][1])
    print(dp[-1])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    X = [int(i) for i in input().split()]
    C_Y = [[int(i) for i in input().split()] for i in range(M)]

    #連続ボーナスの最大値を求める
    bonus = [0 for i in range(N+1)]
    for i in range(M):
        bonus[C_Y[i][0]] = max(bonus[C_Y[i][0]], C_Y[i][1])

    #連続ボーナスの累積和
    for i in range(1, N+1):
        bonus[i] += bonus[i-1]

    #dp[i] = i 回目までのコイントスで得られる最大金額
    dp = [0 for i in range(N+1)]
    for i in range(1, N+1):
        dp[i] = max(dp[i-1]+X[i-1], dp[i-1]+bonus[i])

    print(dp[N])
