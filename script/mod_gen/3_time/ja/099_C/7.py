def main():
    N = int(input())
    dp = [N for _ in range(10**5+1)]
    dp[0] = 0
    for i in range(N+1):
        for j in range(1, 10**5+1):
            if i + j**2 <= N:
                dp[i+j**2] = min(dp[i+j**2], dp[i]+1)
            else:
                break
            if i + j**3 <= N:
                dp[i+j**3] = min(dp[i+j**3], dp[i]+1)
            else:
                break
    print(dp[N])

if __name__ == '__main__':
    main()