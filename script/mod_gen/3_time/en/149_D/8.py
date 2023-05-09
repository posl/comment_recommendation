def main():
    N, K = list(map(int, input().split()))
    R, S, P = list(map(int, input().split()))
    T = input()
    
    #dp[i] = max score if we play the i-th hand
    #dp[i] = max(dp[i-K] + score if we play the i-th hand, dp[i-1])
    dp = [0] * N
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                dp[i] = P
            elif T[i] == 's':
                dp[i] = R
            else:
                dp[i] = S
        else:
            if T[i] == 'r':
                dp[i] = max(dp[i-K] + P, dp[i-1])
            elif T[i] == 's':
                dp[i] = max(dp[i-K] + R, dp[i-1])
            else:
                dp[i] = max(dp[i-K] + S, dp[i-1])
    print(dp[-1])

if __name__ == '__main__':
    main()