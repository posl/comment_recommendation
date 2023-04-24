Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]
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
                dp[3][i][j] += 1
    for i in range(4, n + 1):
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
                    dp[i][j][k] %= 1000000007
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[n][i][j]
    print(ans % 1000000007)

=======
Suggestion 2

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
                if i == 1 and j == 0 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 0:
                    continue
                if i == 2 and j == 0 and k == 0:
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
                    if j == 1 and k == 0 and l == 2:
                        continue
                    if j == 0 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 0:
                        continue
                    dp[i][j][k] += dp[i - 1][k][l]
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N - 1][i][j]
    print(ans % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    N = int(input())
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    mod = 10 ** 9 + 7
    for i in range(N):
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
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= mod

    print(sum(sum(dp[N][i]) for i in range(4)) % mod)

=======
Suggestion 4

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 1 and j == 0 and k == 2:
                    continue
                dp[3][i][j][k] = 1
    for i in range(3, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if l == 0 and k == 1 and m == 2:
                            continue
                        if l == 0 and k == 2 and m == 1:
                            continue
                        if l == 1 and k == 0 and m == 2:
                            continue
                        if l == 1 and k == 2 and m == 0:
                            continue
                        if l == 2 and k == 0 and m == 1:
                            continue
                        if l == 2 and k == 1 and m == 0:
                            continue
                        dp[i+1][j][k][l] += dp[i][j][k][m]
                        dp[i+1][j][k][l] %= MOD
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
    MOD = 10**9+7

    dp = [[0] * 4 for _ in range(N+1)]
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
                if j == 2 and k == 1:
                    continue
                dp[i+1][k] += dp[i][j]
                dp[i+1][k] %= MOD

    ans = 0
    for i in range(4):
        ans += dp[N][i]
        ans %= MOD

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    MOD = 10 ** 9 + 7

    # dp[i][j][k][l]: i文字目まで見たとき、
    # 末尾3文字がj, k, lのときの文字列の個数
    dp = [[[[""] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]

    # 初期化
    for i in range(4):
        for j in range(4):
            for k in range(4):
                dp[3][i][j][k] = 1

    # 答えを求める
    for i in range(3, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if (j == 0 and k == 2 and m == 1) or (j == 0 and k == 1 and m == 2):
                            continue
                        if (j == 0 and k == 2 and l == 1) or (j == 0 and l == 2 and m == 1):
                            continue
                        if (j == 2 and k == 0 and l == 1) or (k == 0 and l == 2 and m == 1):
                            continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD

    # 答えを出力
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
    print(ans % MOD)

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 10**9+7
    # AGC, ACG, GAC, AC, AG, GC
    # 0, 1, 2, 3, 4, 5
    dp = [[[[[0]*6 for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(N+1)]
    dp[0][5][5][5][5] = 1
    for i in range(N):
        for a in range(6):
            for b in range(6):
                for c in range(6):
                    for d in range(6):
                        for e in range(6):
                            if dp[i][a][b][c][d] == 0:
                                continue
                            for f in range(6):
                                if (a == 3 and b == 0 and f == 1) or (a == 3 and c == 0 and f == 1) or (b == 3 and c == 0 and f == 1) or (a == 3 and d == 0 and f == 1) or (b == 3 and d == 0 and f == 1) or (c == 3 and d == 0 and f == 1):
                                    continue
                                if (a == 4 and b == 0 and f == 2) or (a == 4 and c == 0 and f == 2) or (b == 4 and c == 0 and f == 2) or (a == 4 and d == 0 and f == 2) or (b == 4 and d == 0 and f == 2) or (c == 4 and d == 0 and f == 2) or (d == 4 and e == 0 and f == 2):
                                    continue
                                if (a == 5 and b == 0 and f == 3) or (a == 5 and c == 0 and f == 3) or (b == 5 and c == 0 and f == 3) or (a == 5 and d == 0 and f == 3) or (b == 5 and d == 0 and f == 3)

=======
Suggestion 8

def main():
    N = int(input())
    MOD = 10**9+7
    #dp[i][j][k][l] := i文字目まで見て、j文字目がACGTのどれか、k文字目がACGTのどれか、l文字目がACGTのどれかのときの場合の数
    dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i==0 and j==2 and k==1:
                    continue
                if i==0 and j==1 and k==2:
                    continue
                if i==2 and j==0 and k==1:
                    continue
                if i==0 and j==2 and k==2:
                    continue
                if i==2 and j==0 and k==2:
                    continue
                dp[i][j][k][3] = 1
    for i in range(N-1):
        new_dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if dp[j][k][l][3]==0:
                        continue
                    for m in range(4):
                        if j==0 and k==2 and m==1:
                            continue
                        if j==0 and k==1 and m==2:
                            continue
                        if j==2 and k==0 and m==1:
                            continue
                        if j==0 and k==2 and m==2:
                            continue
                        if j==2 and k==0 and m==2:
                            continue
                        new_dp[k][l][m][3] += dp[j][k][l][3]
                        new_dp[k][l][m][3] %= MOD
        dp = new_dp
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k][3]
                ans %= MOD
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    mod = 10**9+7
    #ACGT
    #TACG
    #ATCG
    #AGCG
    #AGTG
    #AGCT
    #AGCA
    #TTCG
    #TCCG
    #TACG
    #TAGG
    #TAGC
    #TAGA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG
    #TACG
    #TATG
    #TATC
    #TATA
    #TTAG
    #TTAC
    #TTAA
    #TTCC
    #TTCA
    #TTCG

=======
Suggestion 10

def main():
    N = int(input())
    MOD = 10**9 + 7
    # dp[i][j][k][l] = i文字目までで、j文字目がAGCのA、k文字目がAGCのG、l文字目がAGCのCである文字列の数
    dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                dp[i][j][k] = 1
    for _ in range(N-3):
        ndp = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 0 and k == 2 and l == 1:
                            continue
                        if j == 0 and k == 1 and l == 2:
                            continue
                        if j == 2 and k == 0 and l == 1:
                            continue
                        ndp[j][k][l] += dp[i][j][k]
                        ndp[j][k][l] %= MOD
        dp = ndp
    print(sum([sum([sum(dp[i][j]) for j in range(4)]) for i in range(4)]) % MOD)
