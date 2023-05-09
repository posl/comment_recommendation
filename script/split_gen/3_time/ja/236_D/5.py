def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [0] * (1 << n)
    for i in range(1 << n):
        for j in range(n):
            if (i >> j) & 1:
                for k in range(j + 1, n):
                    if (i >> k) & 1:
                        b[i] ^= a[j][k]
    dp = [0] * (1 << n)
    for i in range(1 << n):
        for j in range(i):
            dp[i] = max(dp[i], dp[i ^ j] + b[j])
    print(dp[-1])
