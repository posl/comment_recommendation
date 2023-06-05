def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        if dp[i] == -1:
            continue
        for j in range(m):
            dp[i+d[a[j]]] = max(dp[i+d[a[j]]], dp[i]*10+a[j])
    print(dp[n])
