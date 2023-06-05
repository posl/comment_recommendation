def main():
    s = input()
    mod = 10**9 + 7
    dp = [0]*13
    dp[0] = 1
    for si in s:
        if si == '?':
            dp = [sum(dp[10*i+j] for j in range(10)) for i in range(10)]
        else:
            dp = [dp[10*i+(int(si)-0)] for i in range(10)]
    print(dp[5]%mod)

if __name__ == '__main__':
    main()