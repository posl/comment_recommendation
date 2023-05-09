def main():
    n, k = map(int, input().split())
    segments = []
    for i in range(k):
        segments.append(tuple(map(int, input().split())))
    segments.sort()
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(n):
        for segment in segments:
            if i + segment[0] < n:
                dp[i + segment[0]] += dp[i]
                dp[i + segment[0]] %= 998244353
            if i + segment[1] + 1 < n:
                dp[i + segment[1] + 1] -= dp[i]
                dp[i + segment[1] + 1] %= 998244353
    print(dp[n - 1])
