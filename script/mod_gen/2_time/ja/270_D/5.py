def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
            continue
        for a in A:
            if i - a >= 0:
                if dp[i - a] == 0:
                    dp[i] = 1
                    break
    print(dp[N])

if __name__ == '__main__':
    main()