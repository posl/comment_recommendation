def main():
    # Read input
    S = input()
    # Initialize
    dp = [0] * 13
    dp[0] = 1
    # Calculate
    for c in S:
        if c == '?':
            next_dp = [0] * 13
            for i in range(13):
                for j in range(10):
                    next_dp[(i * 10 + j) % 13] += dp[i]
                    next_dp[(i * 10 + j) % 13] %= 10 ** 9 + 7
            dp = next_dp
        else:
            next_dp = [0] * 13
            for i in range(13):
                next_dp[(i * 10 + int(c)) % 13] += dp[i]
                next_dp[(i * 10 + int(c)) % 13] %= 10 ** 9 + 7
            dp = next_dp
    # Output
    print(dp[5])
