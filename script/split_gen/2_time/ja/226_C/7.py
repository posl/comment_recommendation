def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())
    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = max(dp[j - 1] for j in a[i]) + t[i]
    print(dp[n - 1])
