def solve():
    n = int(input())
    v = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    max_v = sum(v)
    dp = [[False for i in range(max_v+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(max_v+1):
            if j >= v[i]:
                dp[i+1][j] = dp[i][j-v[i]] or dp[i][j]
            else:
                dp[i+1][j] = dp[i][j]
    ans = 0
    for i in range(max_v+1):
        if dp[n][i]:
            ans = max(ans, i-sum(c))
    print(ans)

if __name__ == '__main__':
    solve()