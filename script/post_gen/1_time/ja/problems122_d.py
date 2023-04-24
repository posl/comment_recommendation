Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j == 0 and k == 2 and l == 1) or (j == 0 and k == 1 and l == 2):
                        continue
                    if (j == 0 and k == 2 and l == 0) or (j == 0 and k == 0 and l == 2):
                        continue
                    if (j == 2 and k == 0 and l == 1) or (j == 2 and k == 1 and l == 0):
                        continue
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= 10 ** 9 + 7
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N][i][j]
            ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1: continue
                    if j == 0 and k == 1 and l == 2: continue
                    if j == 2 and k == 0 and l == 1: continue
                    if j == 0 and k == 2 and l == 0: continue
                    if j == 2 and k == 0 and l == 0: continue
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= 10 ** 9 + 7
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                dp[3][i][j][k] = 1

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    dp[3][i][j][k] = 0
                if i == 0 and j == 1 and k == 2:
                    dp[3][i][j][k] = 0
                if i == 1 and j == 0 and k == 2:
                    dp[3][i][j][k] = 0

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    dp[3][i][j][k] = 0
                if i == 0 and j == 1 and k == 2:
                    dp[3][i][j][k] = 0
                if i == 1 and j == 0 and k == 2:
                    dp[3][i][j][k] = 0

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    dp[3][i][j][k] = 0
                if i == 0 and j == 1 and k == 2:
                    dp[3][i][j][k] = 0
                if i == 1 and j == 0 and k == 2:
                    dp[3][i][j][k] = 0

    for n in range(4, N+1):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if (i ==

=======
Suggestion 4

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[0]*4 for _ in range(4)] for _ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                if i == 1 and j == 0 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 0:
                    continue
                if i == 2 and j == 0 and k == 0:
                    continue
                dp[3][j][k] += 1
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
                    if j == 1 and k == 0 and l == 2:
                        continue
                    if j == 0 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 0:
                        continue
                    dp[i][k][l] += dp[i-1][j][k]
                    dp[i][k][l] %= MOD
    print(sum(sum(row) for row in dp[N])%MOD)

=======
Suggestion 5

def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[0]*4 for _ in range(4)] for _ in range(n+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i == 0 and j == 2 and k == 1) or (i == 0 and j == 1 and k == 2):
                    continue
                if (i == 0 and j == 2 and k == 0) or (i == 0 and j == 0 and k == 2):
                    continue
                if (i == 0 and j == 1 and k == 0) or (i == 0 and j == 0 and k == 1):
                    continue
                if (i == 1 and j == 0 and k == 2) or (i == 2 and j == 0 and k == 1):
                    continue
                dp[3][i][j] += 1

    for i in range(4,n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j == 0 and k == 2 and l == 1) or (j == 0 and k == 1 and l == 2):
                        continue
                    if (j == 0 and k == 2 and l == 0) or (j == 0 and k == 0 and l == 2):
                        continue
                    if (j == 0 and k == 1 and l == 0) or (j == 0 and k == 0 and l == 1):
                        continue
                    if (j == 1 and k == 0 and l == 2) or (j == 2 and k == 0 and l == 1):
                        continue
                    dp[i+1][k][l] += dp[i][j][k]

    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[n][i][j]
    print(ans%mod)

=======
Suggestion 6

def main():
    N = int(input())
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 1 and j == 0 and k == 2:
                    continue
                if i == 1 and j == 2 and k == 0:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                dp[2][j][k] += 1

    for i in range(3, N):
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
                    dp[i][k][l] += dp[i-1][j][k]

    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N-1][i][j]
    print(ans % (10**9 + 7))

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 0 and k == 2 and l == 2:
                        continue
                    if j == 2 and k == 0 and l == 2:
                        continue
                    dp[i+1][k][l] += dp[i][j][k]
                    dp[i+1][k][l] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[0 for i in range(4)] for j in range(4)] for k in range(N + 1)]
    dp[0][3][3] = 1
    for i in range(N):
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
                    if j == 2 and k == 0 and l == 0:
                        continue
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N][i][j]
            ans %= MOD
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    dp = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 2:
                continue
            if i == 0 and j == 3:
                continue
            if i == 1 and j == 0:
                continue
            if i == 1 and j == 3:
                continue
            if i == 2 and j == 1:
                continue
            dp[i][j] = 1
    for _ in range(N - 1):
        ndp = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == 0 and j == 2 and k == 1:
                        continue
                    if i == 0 and j == 2 and k == 3:
                        continue
                    if i == 0 and j == 3 and k == 1:
                        continue
                    if i == 1 and j == 0 and k == 2:
                        continue
                    if i == 1 and j == 3 and k == 2:
                        continue
                    if i == 2 and j == 1 and k == 0:
                        continue
                    ndp[j][k] += dp[i][j]
        dp = ndp
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[i][j]
    print(ans % (10**9 + 7))

=======
Suggestion 10

def main():
    MOD = 10**9 + 7
    N = int(input())
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0] = [1] * 4
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2 or j == 0 and k == 3 or j == 1 and k == 2:
                    continue
                if j == 2 and k == 0 or j == 3 and k == 0 or j == 2 and k == 1:
                    continue
                dp[i + 1][k] += dp[i][j]
                dp[i + 1][k] %= MOD
    print(sum(dp[N]) % MOD)
