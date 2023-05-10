Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i],Y[i] = map(int,input().split())
    #print(N,M)
    #print(X)
    #print(C)
    #print(Y)
    #print()

    dp = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1,N+1):
        dp[0][i] = X[i-1]

    for i in range(1,M+1):
        for j in range(1,N+1):
            dp[i][j] = max(dp[i][j],dp[i][j-1])
            if j >= C[i-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-C[i-1]]+Y[i-1])
    print(dp[M][N])

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    y = []
    for i in range(m):
        c,yy = map(int,input().split())
        y.append([c,yy])

    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = max(dp[i+1],dp[i]+x[i])
        for j in range(m):
            if i+1 >= y[j][0]:
                dp[i+1] = max(dp[i+1],dp[i+1-y[j][0]]+y[j][1])
    print(dp[n])

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())

    # dp[i][j] = i回目のコイントスで、カウンタの数値がjであるときの、最大のもらえる金額
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][N]
        for j in range(1, N+1):
            dp[i][j] = max(dp[i-1][j-1] + X[i-1], dp[i-1][N])
            for k in range(M):
                if j == C[k]:
                    dp[i][j] = max(dp[i][j], dp[i-1][0] + Y[k])

    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[N][i])
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #print(N, M)
    #print(X)
    #print(C)
    #print(Y)
    dp = [[-1 for i in range(N+1)] for j in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            #print(i, j, dp[i][j])
            # 表
            if i+1 <= N:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
            # 裏
            if i+1 <= N:
                dp[i+1][0] = max(dp[i+1][0], dp[i][j])
            # ボーナス
            for k in range(M):
                if j+1 == C[k]:
                    dp[i+1][0] = max(dp[i+1][0], dp[i][j]+Y[k])
    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[N][i])
    print(ans)

=======
Suggestion 5

def solve(N, M, X, CY):
    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, X[i - 1])
        for j in range(M):
            if i >= CY[j][0]:
                ans = max(ans, X[i - 1] + CY[j][1])
    return ans

N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for i in range(M)]
print(solve(N, M, X, CY))

=======
Suggestion 6

def get_max_reward(n, m, x_list, c_list, y_list):
    # dp[i][j] = i回目のコイントスを終えた時点で、カウンタの数値がjである時の最大報酬
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            # i回目のコイントスで表が出た時
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+x_list[i])
            # i回目のコイントスで裏が出た時
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
            # i回目のコイントスでボーナスが出た時
            for k in range(m):
                if j+1 == c_list[k]:
                    dp[i+1][c_list[k]] = max(dp[i+1][c_list[k]], dp[i][j]+y_list[k])
    return max(dp[-1])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = []
    C = []
    for i in range(M):
        c, y = map(int, input().split())
        Y.append(y)
        C.append(c)
    ans = 0
    for i in range(N):
        ans += X[i]
    for i in range(M):
        tmp = 0
        for j in range(N):
            if C[i] == j + 1:
                tmp += X[j]
        tmp += Y[i]
        if ans < tmp:
            ans = tmp
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    YC = [list(map(int, input().split())) for _ in range(M)]
    YC.sort(key=lambda x: x[1], reverse=True)
    YC.sort(key=lambda x: x[0])
    YC = [[0, 0]] + YC
    YC.append([N+1, 0])
    #print(YC)
    ans = 0
    for i in range(1, M+2):
        if i == 1:
            ans += sum(X)
        else:
            ans += sum(X[YC[i-2][0]-1:YC[i-1][0]-1])
        #print(ans)
        ans += (YC[i][0]-YC[i-1][0])*YC[i-1][1]
        #print(ans)
    print(ans)
    return

main()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)

    # dp[i][j] : i回目のコイントスまでで、カウンタがjになっているときの最大金額
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(N):
        for j in range(N + 1):
            # 表が出たとき
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + X[i])
            # 裏が出たとき
            if j > 0:
                dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j])

        for k in range(M):
            if C[k] == i + 1:
                for j in range(N):
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j] + Y[k])

    print(max(dp[N]))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())

    # DPテーブル
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # DPループ
    for i in range(N + 1):
        for j in range(N + 1):
            if i + j > N:
                break
            # 表が出た時
            if i + 1 <= N:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + X[i])
            # 裏が出た時
            if j + 1 <= N:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
                for k in range(M):
                    if i + j + 1 == C[k]:
                        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + Y[k])

    # 最大値を出力
    print(dp[N][N])
