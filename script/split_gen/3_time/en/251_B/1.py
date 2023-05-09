def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (w + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(w, a[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - a[i]])
    ans = 0
    for i in range(w + 1):
        if dp[i]:
            ans += 1
    print(ans)
