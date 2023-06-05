def main():
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(w+1):
            if j-a[i]>=0:
                dp[i+1][j] |= dp[i][j-a[i]]
            dp[i+1][j] |= dp[i][j]
    ans = 0
    for i in range(w+1):
        if dp[n][i]:
            ans += 1
    print(ans)
