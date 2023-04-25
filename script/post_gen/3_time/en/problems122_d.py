Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if (a, b, c, d) == (0, 1, 2, 3): continue
                        if (a, b, c, d) == (0, 2, 1, 3): continue
                        if (a, b, c, d) == (0, 2, 3, 1): continue
                        if (a, b, c, d) == (2, 0, 1, 3): continue
                        dp[i + 1][d][a][b] += dp[i][a][b][c]
                        dp[i + 1][d][a][b] %= MOD
    ans = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                ans += dp[N][a][b][c]
                ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 1 and m == 2: continue
                        if j == 0 and k == 2 and m == 1: continue
                        if j == 1 and k == 0 and m == 2: continue
                        if j == 1 and k == 2 and m == 0: continue
                        if j == 2 and k == 0 and m == 1: continue
                        if j == 2 and k == 1 and m == 0: continue
                        if j == 0 and k == 1 and l == 2: continue
                        if j == 0 and k == 2 and l == 1: continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                if i == 0 and j == 2 and k == 0:
                    continue
                if i == 2 and j == 0 and k == 2:
                    continue
                dp[2][i][j] += 1

    for i in range(3, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 0 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 2:
                        continue
                    dp[i][j][k] += dp[i - 1][k][l]
                    dp[i][j][k] %= 10 ** 9 + 7

    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N - 1][i][j]
            ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 4

def main():
    mod = 10 ** 9 + 7
    n = int(input())
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 1 and k == 0 and l == 2:
                        continue
                    if j == 1 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 2 and k == 1 and l == 0:
                        continue
                    dp[i + 1][k] += dp[i][j]
                    dp[i + 1][k] %= mod
    print(sum(dp[n]) % mod)

=======
Suggestion 5

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[0]*4 for _ in range(N+1)]
    for i in range(4):
        dp[3][i] = 1
    for i in range(4, N+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3]) % MOD
        dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % MOD
    ans = 0
    for i in range(4):
        ans += dp[N][i]
    print(ans%MOD)

=======
Suggestion 6

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = [1] * 4
    for i in range(1, N):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2 or j == 0 and k == 3 or j == 1 and k == 2 or j == 2 and k == 0:
                    continue
                dp[i][j] += dp[i - 1][k]
    print(sum(dp[N - 1]) % MOD)

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    for i in range(4):
        dp[1][i] = 1
    for i in range(2, N + 1):
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
                dp[i][k] += dp[i - 1][j]
    print(sum(dp[N]) % MOD)

=======
Suggestion 8

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        dp[i] = dp[i-1]*4
        if i >= 3:
            dp[i] -= dp[i-3]
        if i >= 4:
            dp[i] -= dp[i-4]
        dp[i] %= MOD
    print(dp[N])

=======
Suggestion 9

def main():
    N = int(input())
    MOD = 10**9 + 7
    # 0: A, 1: C, 2: G, 3: T
    # dp[i][j][k][l] := i文字目までで、j文字目がACGとなるようにしているか(0: ない, 1: ある)、
    #                   j文字目がACGのどこにあるか(0: A, 1: C, 2: G)、
    #                   j文字目の前の文字がk、j文字目の次の文字がl
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 1 and l == 2: continue
                        if j == 0 and k == 2 and l == 1: continue
                        if j == 1 and k == 0 and l == 2: continue
                        if j == 1 and k == 2 and l == 0: continue
                        if j == 2 and k == 0 and l == 1: continue
                        if j == 2 and k == 1 and l == 0: continue
                        if j == 0 and l == 2 and m == 1: continue
                        if j == 0 and l == 1 and m == 2: continue
                        if j == 1 and l == 2 and m == 0: continue
                        if j == 1 and l == 0 and m == 2: continue
                        if j == 2 and l == 0 and m == 1: continue
                        if j == 2 and l == 1 and m == 0: continue
                        dp[i + 1][j == 3][l][m] += dp[i][j][k][l]
                        dp[i + 1][j

=======
Suggestion 10

def main():
    N = int(input())
    MOD = 10**9+7
    # A, C, G, T
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC, AGGC, AAGC, AGAC, AGTC, AGCC, AGCT, AGCG
    # AGC, ACG, GAC
