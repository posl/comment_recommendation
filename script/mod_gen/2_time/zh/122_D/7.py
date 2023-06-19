def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for len in range(N):
        dp2 = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for a in range(4):
                        if c2 == 0 and c3 == 1 and a == 2: continue
                        if c2 == 1 and c3 == 0 and a == 2: continue
                        if c2 == 0 and c3 == 2 and a == 1: continue
                        if c1 == 0 and c3 == 1 and a == 2: continue
                        if c1 == 0 and c2 == 1 and a == 2: continue
                        dp2[c2][c3][a] += dp[c1][c2][c3]
                        dp2[c2][c3][a] %= mod
        dp = dp2
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[c1][c2][c3]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()