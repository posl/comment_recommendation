def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for n in range(1,N+1):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for c4 in range(4):
                        if c2 == 1 and c3 == 2 and c4 == 0:
                            continue
                        if c2 == 2 and c3 == 1 and c4 == 0:
                            continue
                        if c2 == 1 and c3 == 0 and c4 == 2:
                            continue
                        if c1 == 1 and c3 == 2 and c4 == 0:
                            continue
                        if c1 == 1 and c2 == 2 and c4 == 0:
                            continue
                        dp[n][c2][c3][c4] += dp[n-1][c1][c2][c3]
                        dp[n][c2][c3][c4] %= MOD
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[N][c1][c2][c3]
                ans %= MOD
    print(ans)
