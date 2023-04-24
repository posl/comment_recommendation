Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 1 and m == 2:
                            continue
                        if j == 0 and k == 2 and m == 1:
                            continue
                        if j == 1 and k == 0 and m == 2:
                            continue
                        if j == 1 and k == 2 and m == 0:
                            continue
                        if j == 2 and k == 0 and m == 1:
                            continue
                        if j == 2 and k == 1 and m == 0:
                            continue
                        if l == 0 and k == 1 and m == 2:
                            continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 1 and m == 2:
                            continue
                        if j == 0 and k == 2 and m == 1:
                            continue
                        if j == 1 and k == 0 and m == 2:
                            continue
                        if j == 1 and k == 2 and m == 0:
                            continue
                        if j == 2 and k == 0 and m == 1:
                            continue
                        if j == 2 and k == 1 and m == 0:
                            continue
                        if j == 0 and l == 2 and m == 1:
                            continue
                        if j == 2 and l == 0 and m == 1:
                            continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if dp[i][j][k][l] == 0:
                        continue
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and l == 2:
                            continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
    print(ans % MOD)

=======
Suggestion 4

def main():
    N = int(input())
    MOD = 10**9 + 7

    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i == 0 and j == 1 and k == 2) or (i == 0 and j == 2 and k == 1) or (i == 1 and j == 0 and k == 2):
                    continue
                dp[3][i][j][k] = 1

    for i in range(4, N + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j == 0 and k == 1 and l == 2) or (j == 0 and k == 2 and l == 1) or (j == 1 and k == 0 and l == 2):
                        continue
                    for m in range(4):
                        dp[i][j][k][l] += dp[i - 1][m][j][k]
                        dp[i][j][k][l] %= MOD

    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())

    MOD = 10 ** 9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j == 0 and k == 1 and l == 2) or (j == 0 and k == 2 and l == 1) or (j == 1 and k == 0 and l == 2):
                        continue
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= MOD

    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
    print(ans % MOD)

=======
Suggestion 6

def main():
    n = int(input())
    dp = [[0]*4 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                if j==0 and k==2: continue
                if j==0 and k==1: continue
                if j==1 and k==0: continue
                if j==2 and k==0: continue
                if j==1 and k==2: continue
                dp[i+1][k] += dp[i][j]
                dp[i+1][k] %= 1000000007
    print(sum(dp[n])%1000000007)

=======
Suggestion 7

def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2:
                    continue
                if j == 0 and k == 1:
                    continue
                if j == 1 and k == 0:
                    continue
                if j == 2 and k == 0:
                    continue
                if j == 1 and k == 2:
                    continue
                dp[i + 1][k] += dp[i][j]
                dp[i + 1][k] %= mod
    print(sum(dp[N]) % mod)

=======
Suggestion 8

def main():
    N = int(input())
    MOD = 10**9+7

    # AGC, ACG, GAC, AC?, AG?, CG?
    dp = [[1, 1, 1, 1, 1, 1, 1] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][5] + dp[i-1][6]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][4]) % MOD
        dp[i][2] = (dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % MOD
        dp[i][3] = (dp[i-1][2] + dp[i-1][6]) % MOD
        dp[i][4] = (dp[i-1][1] + dp[i-1][5]) % MOD
        dp[i][5] = (dp[i-1][2] + dp[i-1][6]) % MOD
        dp[i][6] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5]) % MOD
    print(sum(dp[N])%MOD)

=======
Suggestion 9

def dfs(n, s):
    global ans, MOD
    if n == 0:
        ans += 1
        return
    for c in "ACGT":
        if s[-1:] + c in ["AGC", "GAC", "ACG"]:
            continue
        dfs(n - 1, s[-2:] + c)

=======
Suggestion 10

def main():
    N = int(input())
    #dp[i][j][k] := i文字目までで、j文字目の直前にAGCが来ているか、k文字目の直前にAGCが来ているか
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    MOD = 10**9+7

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                if i == 1 and j == 2 and k == 0:
                    continue
                dp[3][i][j] += 1

    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 1 and k == 2 and l == 0:
                        continue
                    dp[i][j][k] += dp[i-1][k][l]
                    dp[i][j][k] %= MOD

    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N][i][j]
            ans %= MOD

    print(ans)
