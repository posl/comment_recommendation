def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    l = 0
    r = 100000000
    while r - l > 0.0000001:
        c = (l + r) / 2
        dp = [0] * (1 << k)
        for i in range(1 << k):
            for j in range(k):
                if (i >> j) & 1:
                    continue
                for t in range(j + 1, k):
                    if (i >> t) & 1:
                        continue
                    dp[i | (1 << j) | (1 << t)] = max(dp[i | (1 << j) | (1 << t)], dp[i] + max(0, 2 * c - ((x[a[j] - 1] - x[a[t] - 1]) ** 2 + (y[a[j] - 1] - y[a[t] - 1]) ** 2) ** 0.5))
        if dp[(1 << k) - 1] > 0:
            l = c
        else:
            r = c
    print(l)
