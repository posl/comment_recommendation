def solve():
    n, x = map(int, input().split())
    coins = [list(map(int, input().split())) for _ in range(n)]
    coins.sort(key=lambda x: x[0])
    dp = [[False for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x+1):
            if not dp[i][j]:
                continue
            for k in range(coins[i][1]+1):
                if j + coins[i][0] * k > x:
                    break
                dp[i+1][j+coins[i][0]*k] = True
    print("Yes" if dp[n][x] else "No")
solve()
