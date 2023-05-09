def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (w + 1)
    for i in range(n):
        for j in range(w, a[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - a[i]] + a[i])
    print(dp[w])
