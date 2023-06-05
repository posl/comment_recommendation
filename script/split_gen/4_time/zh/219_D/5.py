def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    dp[min(X, x+AB[i][0])][min(Y, y+AB[i][1])] = True
    ans = -1
    for x in range(X, X+1):
        for y in range(Y, Y+1):
            if dp[x][y]:
                ans = max(ans, x+y)
    print(ans)
