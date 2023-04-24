Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    A = [0] * (Q + 1)
    B = [0] * (Q + 1)
    C = [0] * (Q + 1)
    A[0] = B[0] = C[0] = 1
    for i in range(Q):
        A[i + 1] = A[i] * 3 % MOD
        B[i + 1] = B[i] * 3 % MOD
        C[i + 1] = C[i] * 3 % MOD
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            ans += B[Q] * C[Q]
            Q -= 1
        elif S[i] == 'B':
            ans += A[Q] * C[Q]
            Q -= 1
        elif S[i] == 'C':
            ans += A[Q] * B[Q]
            Q -= 1
        else:
            ans += A[Q] * B[Q] * 3
            ans += A[Q] * C[Q] * 3
            ans += B[Q] * C[Q] * 3
            Q -= 1
    print(ans % MOD)

=======
Suggestion 2

def main():
    S = input()
    MOD = 10 ** 9 + 7
    Q = S.count('?')
    ans = 0
    A = [0] * (Q + 1)
    B = [0] * (Q + 1)
    C = [0] * (Q + 1)
    for i in range(Q):
        A[i + 1] = pow(3, i, MOD)
        B[i + 1] = pow(3, i, MOD)
        C[i + 1] = pow(3, i, MOD)
    for i in range(Q):
        A[i + 1] = (A[i + 1] + A[i]) % MOD
        B[i + 1] = (B[i + 1] + B[i]) % MOD
        C[i + 1] = (C[i + 1] + C[i]) % MOD
    for i in range(len(S)):
        if S[i] == 'A':
            ans = (ans + B[Q - S[i + 1:].count('?')] + C[Q - S[i + 1:].count('?')]) % MOD
        elif S[i] == 'B':
            ans = (ans + A[Q - S[i + 1:].count('?')] + C[Q - S[i + 1:].count('?')]) % MOD
        elif S[i] == 'C':
            ans = (ans + A[Q - S[i + 1:].count('?')] + B[Q - S[i + 1:].count('?')]) % MOD
        elif S[i] == '?':
            ans = (ans + A[Q - S[i + 1:].count('?') - 1] + B[Q - S[i + 1:].count('?') - 1] + C[Q - S[i + 1:].count('?') - 1]) % MOD
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    MOD = 10**9 + 7
    n = len(S)
    abc = [0] * n
    for i in range(n):
        if S[i] == 'A':
            abc[i] = 1
        elif S[i] == 'B':
            abc[i] = 2
        elif S[i] == 'C':
            abc[i] = 3
    #print(abc)
    cnt = [0, 0, 0, 0]
    for i in range(n):
        cnt[abc[i]] += 1
    #print(cnt)
    ans = 0
    q = S.count('?')
    for i in range(n):
        if abc[i] == 0:
            ans += cnt[1] * pow(3, q - 1, MOD) + cnt[2] * pow(3, q - 1, MOD) + cnt[3] * pow(3, q - 1, MOD)
            ans %= MOD
            q -= 1
        elif abc[i] == 1:
            ans += cnt[2] * pow(3, q, MOD) + cnt[3] * pow(3, q, MOD)
            ans %= MOD
        elif abc[i] == 2:
            ans += cnt[1] * pow(3, q, MOD) + cnt[3] * pow(3, q, MOD)
            ans %= MOD
        elif abc[i] == 3:
            ans += cnt[1] * pow(3, q, MOD) + cnt[2] * pow(3, q, MOD)
            ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    ans = 0
    for i in range(3**Q):
        T = ''
        j = i
        for c in S:
            if c == '?':
                T += chr(ord('A') + j % 3)
                j //= 3
            else:
                T += c
        cnt = 0
        for k in range(len(T) - 2):
            if T[k] == 'A' and T[k+1] == 'B' and T[k+2] == 'C':
                cnt += 1
        ans += cnt
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    # 10^9 + 7
    MOD = 10**9 + 7
    # 文字列入力
    S = input().rstrip()
    # ?の個数
    Q = S.count("?")
    # 3^Q
    Q3 = pow(3, Q, MOD)
    # 3^Qの和
    Q3sum = 0
    # 累積和
    Asum = [0] * (len(S) + 1)
    Bsum = [0] * (len(S) + 1)
    Csum = [0] * (len(S) + 1)
    # 累積和作成
    for i in range(len(S)):
        if S[i] == "A":
            Asum[i + 1] = Asum[i] + 1
            Bsum[i + 1] = Bsum[i]
            Csum[i + 1] = Csum[i]
        elif S[i] == "B":
            Asum[i + 1] = Asum[i]
            Bsum[i + 1] = Bsum[i] + 1
            Csum[i + 1] = Csum[i]
        elif S[i] == "C":
            Asum[i + 1] = Asum[i]
            Bsum[i + 1] = Bsum[i]
            Csum[i + 1] = Csum[i] + 1
        else:
            Asum[i + 1] = Asum[i]
            Bsum[i + 1] = Bsum[i]
            Csum[i + 1] = Csum[i]
    # ABC数の和
    ABCsum = 0
    # ?をA,B,Cに置き換える
    for i in range(len(S)):
        if S[i] == "?":
            # ?をAに置き換える場合
            A = Asum[i] + 1
            B = Bsum[i]
            C = Csum[i]
            ABCsum += A * B * C * Q3
            ABCsum %= MOD
            # ?をBに置き換える場合
            A = Asum[i]

=======
Suggestion 6

def main():
    S = input()
    Q = S.count("?")
    MOD = 10**9 + 7
    # dp[i][j][k]: i文字目まで見て、Aがj個、Bがk個あるときのABC数
    dp = [[[0 for _ in range(Q+1)] for _ in range(Q+1)] for _ in range(Q+1)]
    for i in range(len(S)):
        if S[i] == "A":
            dp[i+1][1][0] = (dp[i][0][0] + 1) % MOD
            dp[i+1][1][0] += dp[i][1][0]
            dp[i+1][1][0] %= MOD
            for j in range(1, Q+1):
                dp[i+1][j+1][0] = (dp[i][j][0] + 1) % MOD
                dp[i+1][j+1][0] += dp[i][j+1][0]
                dp[i+1][j+1][0] %= MOD
            for k in range(1, Q+1):
                dp[i+1][1][k] = (dp[i][0][k] + 1) % MOD
                dp[i+1][1][k] += dp[i][1][k]
                dp[i+1][1][k] %= MOD
        elif S[i] == "B":
            for j in range(1, Q+1):
                dp[i+1][j][1] = (dp[i][j][0] + 1) % MOD
                dp[i+1][j][1] += dp[i][j][1]
                dp[i+1][j][1] %= MOD
            for k in range(1, Q+1):
                dp[i+1][0][k] = (dp[i][0][k] + 1) % MOD
                dp[i+1][0][k] += dp[i][0][k-1]
                dp[i+1][0][k] %= MOD
            for j in range(1, Q+1):
                for k in range(1, Q+1):
                    dp[i+1][j][k] = (dp[i][j][

=======
Suggestion 7

def main():
    S = input()
    mod = 10**9 + 7
    Q = S.count('?')
    n = len(S)
    ABC = [0]*n
    ABC[0] = 1
    for i in range(1,n):
        if S[i-1] == '?':
            ABC[i] = ABC[i-1]*3
        else:
            ABC[i] = ABC[i-1]
    print(ABC)
    ans = 0
    for i in range(n):
        if S[i] == 'A':
            ans += ABC[i]*pow(3,Q,mod)
        elif S[i] == 'B':
            ans += ABC[i]*pow(3,Q,mod)
        elif S[i] == 'C':
            ans += ABC[i]*pow(3,Q,mod)
        elif S[i] == '?':
            ans += ABC[i]*pow(3,Q-1,mod)
    print(ans%mod)

=======
Suggestion 8

def main():
    S = input()
    Q = S.count("?")
    mod = 10**9+7
    #print(S)
    #print(Q)
    if Q == 0:
        #print("Q=0")
        #print(S)
        #print(len(S))
        #print(S[0])
        #print(S[1])
        #print(S[2])
        #print(S[3])
        #print(S[4])
        #print(S[5])
        #print(S[6])
        #print(S[7])
        #print(S[8])
        #print(S[9])
        #print(S[10])
        #print(S[11])
        #print(S[12])
        #print(S[13])
        #print(S[14])
        #print(S[15])
        #print(S[16])
        #print(S[17])
        #print(S[18])
        #print(S[19])
        #print(S[20])
        #print(S[21])
        #print(S[22])
        #print(S[23])
        #print(S[24])
        #print(S[25])
        #print(S[26])
        #print(S[27])
        #print(S[28])
        #print(S[29])
        #print(S[30])
        #print(S[31])
        #print(S[32])
        #print(S[33])
        #print(S[34])
        #print(S[35])
        #print(S[36])
        #print(S[37])
        #print(S[38])
        #print(S[39])
        #print(S[40])
        #print(S[41])
        #print(S[42])
        #print(S[43])
        #print(S[44])
        #print(S[45])
        #print(S[46])
        #print(S[47])
        #print(S[48])
        #print(S[49])
        #print(S[50])
        #print(S[51])
        #print(S[52])
        #print(S[53])
        #print(S[54])
        #print(S[55])
        #print(S[56])
        #print(S[57])
        #print(S[58])
        #print(S[59])
        #print(S[60])
        #print(S[61])
        #print(S[62

=======
Suggestion 9

def main():
    s = input()
    mod = 10**9+7
    #dp[i][j] = i文字目まで見たときに、j文字目に何を入れるかの場合の数
    #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    #dp[i-1][j-1] = 3文字目にAを入れる
    #dp[i-1][j] = 3文字目にBを入れる
    #dp[i-1][j+1] = 3文字目にCを入れる
    #dp[0][0] = 1
    dp = [[0]*4 for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(4):
            if s[i] == '?':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            elif j == 1 and s[i] == 'A':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            elif j == 2 and s[i] == 'B':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            elif j == 3 and s[i] == 'C':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            else:
                dp[i+1][j] = dp[i][j]
            dp[i+1][j] %= mod
    print(dp[len(s)][2])

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    # 3**N は最大でも 3**10**5 = 3**10**5 であり、これは 10**15 であり、
    # 10**15 は int の最大値である 10**18 より小さい。
    # したがって、3**N を計算しておいてもオーバーフローしない。
    # また、3**N は 3**Q に等しい。
    Q = S.count('?')
    MOD = 10**9 + 7
    ans = 0
    # 3**Q 通りの文字列それぞれについて、ABC 数を求める。
    for i in range(3**Q):
        # 3**Q 通りの文字列それぞれについて、
        # 3**Q 通りの文字列のうち i 番目の文字列における
        # 「? を A, B, C のいずれかに置き換えたときの文字列」を求める。
        # このとき、i は 3 進数とみなして、i の各桁を 0, 1, 2 とみなす。
        # 例えば、i = 3 ならば、i の各桁は 1, 0, 0 となる。
        # このとき、3**Q 通りの文字列のうち i 番目の文字列における
        # 「? を A, B, C のいずれかに置き換えたときの文字列」は
        # ?AC である。
        # このとき、i の各桁は 1, 0, 0 となる。
        # このとき、3**Q 通りの文字列のうち i 番目の文字列における
        # 「? を A, B, C のいずれかに
