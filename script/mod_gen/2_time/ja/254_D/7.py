def main():
    n = int(input())
    l = []
    for i in range(1, int(n ** 0.5) + 1):
        l.append(i * i)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in l:
            if i - j < 0:
                break
            dp[i] += dp[i - j]
        dp[i] += 1
    print(dp[n])

if __name__ == '__main__':
    main()