def main():
    # Get input here
    N, K = map(int, input().strip().split())
    segments = []
    for i in range(K):
        segments.append(list(map(int, input().strip().split())))
    # Solve problems
    dp = [0] * N
    dp[0] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(1, N):
        for segment in segments:
            left = i - segment[1]
            right = i - segment[0]
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            dp[i] += dpsum[right] - dpsum[left]
        dp[i] %= 998244353
        dpsum[i+1] = dpsum[i] + dp[i]
    # Print output here
    print(dp[N-1])

if __name__ == '__main__':
    main()