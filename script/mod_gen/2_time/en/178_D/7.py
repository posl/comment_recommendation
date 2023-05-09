def get_num_sequences(S):
    MOD = 10**9 + 7
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(3, S + 1):
        dp[i] = dp[i - 1] + dp[i - 3]
        dp[i] %= MOD
    return dp[S]
print(get_num_sequences(int(input())))

if __name__ == '__main__':
    get_num_sequences()