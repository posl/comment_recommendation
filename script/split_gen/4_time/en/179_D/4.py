def main():
    n, k = map(int, input().split())
    segs = []
    for i in range(k):
        segs.append(list(map(int, input().split())))
    segs.sort()
    dp = [0] * n
    dp[0] = 1
    dpsum = [0] * n
    dpsum[0] = 1
    for i in range(1, n):
        for seg in segs:
            l = i - seg[1]
            r = i - seg[0]
            if r < 0:
                continue
            l = max(l, 0)
            dp[i] += dpsum[r] - dpsum[l - 1]
            dp[i] %= 998244353
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= 998244353
    print(dp[-1])
    return
