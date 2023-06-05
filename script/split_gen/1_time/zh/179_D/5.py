def main():
    n, k = map(int, input().split())
    lr = []
    for i in range(k):
        lr.append(list(map(int, input().split())))
    dp = [0]*n
    dp[0] = 1
    for i in range(n):
        for j in range(k):
            if i + lr[j][0] < n:
                dp[i+lr[j][0]] += dp[i]
            if i + lr[j][1] + 1 < n:
                dp[i+lr[j][1]+1] -= dp[i]
    dp = dp[:-1]
    for i in range(1, n):
        dp[i] += dp[i-1]
    print(dp[-1]%998244353)
main()
