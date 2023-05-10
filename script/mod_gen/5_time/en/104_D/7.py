def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    dp = [1]
    for i in range(Q):
        dp.append(dp[-1] * 3 % MOD)
    ans = 0
    cnt = 0
    for i, s in enumerate(S):
        if s == 'A':
            cnt += dp[i]
        elif s == 'B':
            ans += cnt * dp[Q - i]
        elif s == 'C':
            ans += cnt * dp[Q - i] * dp[Q - i]
    print(ans % MOD)

if __name__ == '__main__':
    main()