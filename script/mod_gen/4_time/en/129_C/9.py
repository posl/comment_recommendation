def main():
    N, M = map(int, input().split())
    broken_steps = [int(input()) for _ in range(M)]
    broken_steps.append(N+1)
    broken_steps.sort()
    #print(broken_steps)
    
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in broken_steps:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()