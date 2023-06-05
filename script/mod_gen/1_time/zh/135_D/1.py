def main():
    input_str = input()
    input_str = input_str[::-1]
    input_len = len(input_str)
    mod = 10**9 + 7
    dp = [0] * 13
    dp[0] = 1
    for i in range(input_len):
        next_dp = [0] * 13
        if input_str[i] != "?":
            num = int(input_str[i])
            for j in range(13):
                next_dp[(j * 10 + num) % 13] += dp[j]
                next_dp[(j * 10 + num) % 13] %= mod
        else:
            for j in range(10):
                for k in range(13):
                    next_dp[(k * 10 + j) % 13] += dp[k]
                    next_dp[(k * 10 + j) % 13] %= mod
        dp = next_dp
    print(dp[5])

if __name__ == '__main__':
    main()