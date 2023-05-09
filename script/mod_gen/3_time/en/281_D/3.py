def solve():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (d + 1)
    for i in range(d + 1):
        for j in range(k):
            if i - a[j] >= 0:
                dp[i] = dp[i] or not dp[i - a[j]]
    if dp[d]:
        print(d)
    else:
        print(-1)

if __name__ == '__main__':
    solve()