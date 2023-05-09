def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    n = int(input())
    t = [0]*n
    k = [0]*n
    a = [0]*n
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())
    dp = [0]*n
    dp[0] = t[0]
    for i in range(1, n):
        dp[i] = t[i] + dp[i-1]
        for j in range(k[i]):
            dp[i] = min(dp[i], dp[a[i][j]-1] + t[i])
    print(dp[n-1])
