def solve():
    N = int(input())
    X, Y = map(int, input().split())
    #dp[i][j][k]表示用前i个便当，j个章鱼烧，k个鱼形蛋糕
    #能否满足条件
    dp = [[[False for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = True
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(X+1):
            for k in range(Y+1):
                if j >= a and k >= b:
                    dp[i+1][j][k] = dp[i][j][k] or dp[i][j-a][k-b]
                else:
                    dp[i+1][j][k] = dp[i][j][k]
    if dp[N][X][Y]:
        print("Yes")
    else:
        print("No")
solve()
