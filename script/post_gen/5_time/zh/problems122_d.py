Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [0]*64
    for i in range(64):
        if i & 0b0111 == 0b0111:
            continue
        if i & 0b1001 == 0b1001:
            continue
        if i & 0b1100 == 0b1100:
            continue
        dp[i] = 1
    for i in range(N-3):
        dp2 = [0]*64
        for j in range(64):
            for k in range(4):
                dp2[(j<<1|k)&0b1111] += dp[j]
                dp2[(j<<1|k)&0b1111] %= MOD
        dp = dp2
    print(sum(dp)%MOD)

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 1 and l == 2 and m == 3:
                            continue
                        if k == 2 and l == 1 and m == 3:
                            continue
                        if k == 1 and l == 3 and m == 2:
                            continue
                        if j == 1 and l == 2 and m == 3:
                            continue
                        if j == 1 and k == 2 and m == 3:
                            continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    mod = 10 ** 9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for _ in range(N):
        dp2 = [[[0] * 4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if (j == 0 and k == 1 and l == 2) or (j == 0 and k == 2 and l == 1) or (j == 1 and k == 0 and l == 2) or (i == 0 and k == 1 and l == 2) or (i == 0 and j == 1 and l == 2):
                            continue
                        dp2[j][k][l] += dp[i][j][k]
                        dp2[j][k][l] %= mod
        dp = dp2
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dp[3][0][0] = 1
    mod = 10 ** 9 + 7

    for i in range(n):
        temp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 1 and l == 2 and m == 3: continue
                        if k == 2 and l == 1 and m == 3: continue
                        if k == 1 and l == 3 and m == 2: continue
                        if j == 1 and l == 2 and m == 3: continue
                        if j == 1 and k == 2 and m == 3: continue
                        temp[k][l][m] += dp[j][k][l]
                        temp[k][l][m] %= mod
        dp = temp

    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    mod = 10**9+7
    dp = [0] * (4**3)
    #dp[i] := 末尾3文字がAGCでない文字列の個数
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                #AGCでない文字列でない場合
                if (c2 == 0 and c3 == 2) or (c2 == 2 and c3 == 0) or (c1 == 0 and c3 == 2):
                    continue
                dp[c1*16+c2*4+c3] = 1

    for i in range(4**3):
        #末尾につける文字
        c1 = i // 16
        #末尾から2番目につける文字
        c2 = (i//4) % 4
        #末尾から3番目につける文字
        c3 = i % 4
        for a in range(4):
            #追加する文字
            if (c2 == 0 and c3 == 2) or (c2 == 2 and c3 == 0) or (c1 == 0 and c3 == 2):
                continue
            if (a == 0 and c2 == 2 and c3 == 1) or (a == 0 and c2 == 1 and c3 == 2):
                continue
            dp[a*16+c1*4+c2] += dp[i]
            dp[a*16+c1*4+c2] %= mod
    ans = 0
    for i in range(4**3):
        ans += dp[i]
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    mod = 10**9+7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if m == 1 and k == 2 and l == 0: continue
                        if m == 2 and k == 1 and l == 0: continue
                        if m == 1 and k == 0 and l == 2: continue
                        if j == 1 and m == 2 and l == 0: continue
                        if j == 1 and k == 2 and m == 0: continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    #dp[i][j][k][l] := 长度为i，最后三个字母为jkl的字符串的数量
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    #初始化
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == 0 and k == 1 and l == 2:
                    continue
                if j == 0 and k == 2 and l == 1:
                    continue
                if j == 1 and k == 0 and l == 2:
                    continue
                dp[3][j][k][l] = 1
    #dp
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 0 and j == 1 and m == 2:
                            continue
                        if k == 1 and l == 0 and m == 2:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= 1000000007
    #答案
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= 1000000007
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    mod = 10 ** 9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    # dp[i][j][k] := 3文字目がi, 2文字目がj, 1文字目がkであるような文字列の個数
    # i,j,k = 0,1,2,3 := A,C,G,T
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 1 and j == 0 and k == 2:
                    continue
                dp[i][j][k] = 1
    for _ in range(3, N):
        next_dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 0 and k == 1 and l == 2:
                            continue
                        if j == 0 and k == 2 and l == 1:
                            continue
                        if i == 0 and k == 1 and l == 2:
                            continue
                        if i == 0 and j == 1 and l == 2:
                            continue
                        if i == 0 and j == 1 and k == 2:
                            continue
                        next_dp[j][k][l] += dp[i][j][k]
                        next_dp[j][k][l] %= mod
        dp = next_dp
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
    dp[3][3][3] = 1
    for i in range(n):
        temp = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if m == 0 and k == 1 and l == 2:
                            continue
                        if m == 1 and k == 0 and l == 2:
                            continue
                        if m == 0 and k == 2 and l == 1:
                            continue
                        if m == 0 and j == 1 and l == 2:
                            continue
                        if m == 0 and k == 1 and j == 2:
                            continue
                        temp[k][l][m] += dp[j][k][l]
                        temp[k][l][m] %= mod
        dp = temp
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    #dp[i][j][k][l] は、長さiの文字列で、末尾から3文字がjklであるものの個数を表す
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    #初期値
    dp[0][3][3][3] = 1

    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 1 and l == 0 and m == 2:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
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
