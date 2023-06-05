def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for length in range(N):
        dp2 = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for a in range(4):
                        if a == 2 and c1 == 1 and c2 == 0:
                            continue
                        if a == 2 and c1 == 0 and c2 == 1:
                            continue
                        if a == 1 and c1 == 2 and c2 == 0:
                            continue
                        if a == 2 and c1 == 1 and c3 == 0:
                            continue
                        if a == 2 and c2 == 1 and c3 == 0:
                            continue
                        dp2[c1][c2][a] += dp[c2][c3][a]
                        dp2[c1][c2][a] %= mod
        dp = dp2
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[c1][c2][c3]
                ans %= mod
    print(ans)
