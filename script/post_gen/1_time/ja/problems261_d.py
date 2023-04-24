Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for _ in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #print(N, M)
    #print(X)
    #print(C, Y)

    #dp[i][j] := i回目までのコイントスで、カウンタの数値がjのときにもらえる最大金額
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j == 0:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i])
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + Y[C.index(j)])
    #print(dp)
    print(max(dp[N]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    # print(N, M)
    # print(X)
    # print(C)
    # print(Y)

    ans = 0
    for i in range(N):
        ans += X[i]
        for j in range(M):
            if i >= C[j] - 1:
                ans += Y[j] * (i - C[j] + 2)
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + x[i - 1]
        for j in range(m):
            if i - c[j] >= 0:
                dp[i] = max(dp[i], dp[i - c[j]] + y[j])
    print(dp[n])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_, y_ = map(int, input().split())
        c.append(c_)
        y.append(y_)
    dp = [0] * (n+1)
    for i in range(n):
        dp[i+1] = max(dp[i+1], dp[i] + x[i])
        for j in range(m):
            if i + c[j] <= n:
                dp[i+c[j]] = max(dp[i+c[j]], dp[i] + y[j])
    print(dp[n])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0 for _ in range(N)]
    Y = [0 for _ in range(N)]
    for _ in range(M):
        c, y = map(int, input().split())
        C[c-1] = c
        Y[c-1] = y
    dp = [0 for _ in range(N+1)]
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        dp[C[i]] = max(dp[C[i]], dp[i]+Y[i])
    print(dp[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C_Y = [list(map(int, input().split())) for _ in range(M)]
    C_Y.sort(key=lambda x: x[0])
    C, Y = zip(*C_Y)
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + 1 < C[j]:
                break
            dp[i + 1] = max(dp[i + 1], dp[i + 1 - C[j]] + Y[j])
    print(dp[N])

=======
Suggestion 8

def main():
    # 入力
    N,M = map(int,input().split())
    X = [int(x) for x in input().split()]
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i],Y[i] = map(int,input().split())
    # 処理
    # dp[i] = i回目までのコイントスでもらえる最大の金額
    dp = [0]*(N+1)
    # 連続ボーナスを受け取る
    for i in range(M):
        dp[C[i]] = max(dp[C[i]],Y[i])
    # 連続ボーナスを受け取る
    for i in range(N):
        dp[i+1] = max(dp[i+1],dp[i])
    # 連続ボーナスを受け取っていない場合の金額を計算
    for i in range(N):
        if dp[i+1] == dp[i]:
            dp[i+1] = dp[i] + X[i]
    # 出力
    print(max(dp))

=======
Suggestion 9

def read_int():
    return int(input())
