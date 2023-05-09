def main():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    dp = [0] * (1 << n)
    for i in range(1 << n):
        for j in range(n):
            if (i >> j) & 1:
                continue
            for k in range(j + 1, n):
                if (i >> k) & 1:
                    continue
                dp[i | (1 << j) | (1 << k)] = max(dp[i | (1 << j) | (1 << k)], dp[i] + a[j][k])
    print(dp[-1])

if __name__ == '__main__':
    main()