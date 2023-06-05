def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0]*4 for i in range(4)] for j in range(4)] for k in range(N+1)]
    dp[0][3][3][3] = 1
    for length in range(N):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for new in range(4):
                        if c2 == 0 and c3 == 1 and new == 2:
                            continue
                        if c2 == 1 and c3 == 0 and new == 2:
                            continue
                        if c2 == 0 and c3 == 2 and new == 1:
                            continue
                        if c1 == 0 and c3 == 1 and new == 2:
                            continue
                        if c1 == 0 and c2 == 1 and new == 2:
                            continue
                        dp[length+1][c2][c3][new] += dp[length][c1][c2][c3]
                        dp[length+1][c2][c3][new] %= MOD
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[N][c1][c2][c3]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()