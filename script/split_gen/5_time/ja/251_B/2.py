def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    dp = [[False for _ in range(w+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(w+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j+a[i] <= w:
                    dp[i+1][j+a[i]] = True
    ans = 0
    for i in range(w+1):
        if dp[n][i]:
            ans += 1
    print(ans)
