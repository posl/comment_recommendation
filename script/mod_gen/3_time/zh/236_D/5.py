def main():
    n = int(input())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    dp = [0] * (1 << n)
    for s in range(1 << n):
        x = bin(s).count('1')
        for i in range(n):
            if s >> i & 1:
                for j in range(i + 1, n):
                    if s >> j & 1:
                        dp[s] += a[x - 1][i + j - x]
    for s in range(1, 1 << n):
        for t in range(s):
            if s & t == t:
                dp[s] = max(dp[s], dp[t] + dp[s ^ t])
    print(dp[(1 << n) - 1])

if __name__ == '__main__':
    main()