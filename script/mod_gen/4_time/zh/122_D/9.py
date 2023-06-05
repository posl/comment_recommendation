def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
    dp[0][3][3][3] = 1
    for len in range(n):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for a in range(4):
                        if c2==0 and c3==1 and a==2: continue
                        if c2==1 and c3==0 and a==2: continue
                        if c2==0 and c3==2 and a==1: continue
                        if c1==0 and c3==1 and a==2: continue
                        if c1==0 and c2==1 and a==2: continue
                        dp[len+1][c2][c3][a] += dp[len][c1][c2][c3]
                        dp[len+1][c2][c3][a] %= mod
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += dp[n][c1][c2][c3]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()