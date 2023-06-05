Synthesizing 10/10 solutions

=======
Suggestion 1

def is_ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True

=======
Suggestion 2

def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for c1 in "ACGT":
            for c2 in "ACGT":
                for c3 in "ACGT":
                    if c1 == "A" and c2 == "G" and c3 == "C":
                        continue
                    if c1 == "A" and c2 == "C" and c3 == "G":
                        continue
                    if c1 == "G" and c2 == "A" and c3 == "C":
                        continue
                    if c1 == "A" and c2 == "G" and c3 == "T":
                        continue
                    if c1 == "A" and c2 == "T" and c3 == "G":
                        continue
                    if c1 == "G" and c2 == "A" and c3 == "T":
                        continue
                    if c1 == "G" and c2 == "T" and c3 == "A":
                        continue
                    if c1 == "T" and c2 == "G" and c3 == "A":
                        continue
                    if c1 == "C" and c2 == "G" and c3 == "A":
                        continue
                    if c1 == "G" and c2 == "C" and c3 == "A":
                        continue
                    dp[i] += dp[i - 1]
                    dp[i] %= mod
    print(dp[N])

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    #dp[i][j][k][l]:i桁目にjklが来る場合の数
    #dp[0][0][0][0] = 1
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 0 and k == 0:
                    continue
                if i == 0 and j == 0 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 0:
                    continue
                if i == 1 and j == 0 and k == 0:
                    continue
                dp[3][i][j][k] = 1
    for n in range(4,N+1):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 0 and k == 1 and l == 2:
                            continue
                        if j == 0 and k == 2 and l == 1:
                            continue
                        if j == 1 and k == 0 and l == 2:
                            continue
                        if i == 0 and k == 1 and l == 2:
                            continue
                        if i == 0 and j == 1 and l == 2:
                            continue
                        dp[n][j][k][l] += dp[n-1][i][j][k]
                        dp[n][j][k][l] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    mod = 10 ** 9 + 7
    S = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                S[3][c1][c2][c3] = 1
    for n in range(4, N + 1):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for c4 in range(4):
                        if c2 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c2 == 2 and c3 == 0 and c4 == 1:
                            continue
                        if c2 == 0 and c3 == 1 and c4 == 2:
                            continue
                        if c1 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c1 == 0 and c2 == 2 and c4 == 1:
                            continue
                        S[n][c2][c3][c4] += S[n - 1][c1][c2][c3]
                        S[n][c2][c3][c4] %= mod
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += S[N][c1][c2][c3]
                ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    mod = 10**9+7
    dp = [0]*64
    # 0:A,1:C,2:G,3:T
    for i in range(64):
        if i & 1 and i >> 1 & 1 and i >> 2 & 1:
            continue
        if i & 1 and i >> 1 & 1 and i >> 3 & 1:
            continue
        if i & 1 and i >> 2 & 1 and i >> 3 & 1:
            continue
        if i >> 1 & 1 and i >> 2 & 1 and i >> 3 & 1:
            continue
        dp[i] = 1
    for i in range(4,n+1):
        ndp = [0]*64
        for j in range(64):
            for k in range(4):
                nj = (j << 1 | k) & 63
                if nj & 1 and nj >> 1 & 1 and nj >> 2 & 1:
                    continue
                if nj & 1 and nj >> 1 & 1 and nj >> 3 & 1:
                    continue
                if nj & 1 and nj >> 2 & 1 and nj >> 3 & 1:
                    continue
                if nj >> 1 & 1 and nj >> 2 & 1 and nj >> 3 & 1:
                    continue
                ndp[nj] += dp[j]
                ndp[nj] %= mod
        dp = ndp
    print(sum(dp) % mod)

=======
Suggestion 6

def main():
    N = int(input())
    MOD = 10**9 + 7
    #dp[i][j][k][l]：字符串的长度为i，最后三个字符为jkl的字符串的数量
    #jkl是"AGC"以外的字符串
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == 0 and k == 2 and l == 1:
                    continue
                if j == 0 and k == 1 and l == 2:
                    continue
                if j == 2 and k == 0 and l == 1:
                    continue
                dp[3][j][k][l] = 1
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and l == 2 and m == 1:
                            continue
                        if k == 2 and l == 0 and m == 1:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 10**9+7

    #dp[i][j][k][l] := 长度为iで末尾3文字がjklである文字列の個数
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]

    #初期化
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j==0 and k==1 and l==2:
                    continue
                if j==0 and k==2 and l==1:
                    continue
                if j==1 and k==0 and l==2:
                    continue
                dp[3][j][k][l] = 1

    for i in range(4,N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k==0 and l==1 and m==2:
                            continue
                        if k==0 and l==2 and m==1:
                            continue
                        if j==0 and l==1 and m==2:
                            continue
                        if k==0 and j==1 and m==2:
                            continue
                        if k==0 and l==1 and j==2:
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= MOD

    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD

    print(ans)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    NG = set(['AGC', 'GAC', 'ACG'])
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if NG.__contains__(''.join([chr(j + ord('A')), chr(k + ord('A')), chr(l + ord('A'))])):
                            continue
                        if NG.__contains__(''.join([chr(j + ord('A')), chr(k + ord('A')), chr(m + ord('A'))])):
                            continue
                        if NG.__contains__(''.join([chr(j + ord('A')), chr(l + ord('A')), chr(m + ord('A'))])):
                            continue
                        if NG.__contains__(''.join([chr(k + ord('A')), chr(l + ord('A')), chr(m + ord('A'))])):
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

=======
Suggestion 10

def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for n in range(N):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 0 and k == 1 and l == 2: continue
                        if j == 1 and k == 0 and l == 2: continue
                        if j == 0 and k == 2 and l == 1: continue
                        if i == 0 and k == 1 and l == 2: continue
                        if i == 0 and j == 1 and l == 2: continue
                        dp[n+1][j][k][l] += dp[n][i][j][k]
                        dp[n+1][j][k][l] %= mod
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= mod
    print(ans)
