def main():
    s = input()
    n = len(s)
    dp = [0] * n
    for i in range(n):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            if i == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    print(max(dp))

if __name__ == '__main__':
    main()