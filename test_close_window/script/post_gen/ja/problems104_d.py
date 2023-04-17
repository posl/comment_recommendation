Synthesizing 10/10 solutions

=======

def main():
    S = input()
    mod = 10 ** 9 + 7
    Q = S.count("?")
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    D = S.count("?")
    ans = 0
    for i in range(3 ** Q):
        t = i
        s = S
        for j in range(Q):
            if t % 3 == 0:
                s = s.replace("?", "A", 1)
            elif t % 3 == 1:
                s = s.replace("?", "B", 1)
            else:
                s = s.replace("?", "C", 1)
            t //= 3
        cnt = 0
        for j in range(len(s) - 2):
            if s[j] == "A" and s[j + 1] == "B" and s[j + 2] == "C":
                cnt += 1
        ans += cnt
    print(ans % mod)

=======

def main():
    mod = 10 ** 9 + 7
    s = input()
    n = len(s)
    a = 0
    b = 0
    c = 0
    q = 0
    for i in range(n):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += a
        elif s[i] == "C":
            c += b
        else:
            c = c * 3 + b
            b = b * 3 + a
            a = a * 3
            q += 1
        a %= mod
        b %= mod
        c %= mod
    print(c)

=======

def abc104_d():
    mod = 10**9+7
    s = input()
    n = len(s)
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
    dp[0][3][3][3] = 1
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
                    if s[i] == "?":
                        for m in range(4):
                            dp[i+1][m][j][k] = (dp[i+1][m][j][k] + dp[i][l][j][k]) % mod
                    else:
                        dp[i+1][int(s[i])] [j][k] = (dp[i+1][int(s[i])] [j][k] + dp[i][l][j][k]) % mod
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans = (ans + dp[n][i][j][k]) % mod
    print(ans)

=======

def main():
    S = input()
    Q = S.count("?")
    MOD = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for s in S:
        if s == "A":
            a += 1
        elif s == "B":
            b += a
        elif s == "C":
            c += b
        else:
            c = c * 3 + b
            b = b * 3 + a
            a = a * 3
            c %= MOD
            b %= MOD
            a %= MOD
    print(c)

=======

def main():
    s = input()
    q = s.count("?")
    mod = 10**9+7
    ans = 0
    for i in range(3**q):
        tmp = s
        for j in range(q):
            if i // 3**j % 3 == 0:
                tmp = tmp.replace("?", "A", 1)
            elif i // 3**j % 3 == 1:
                tmp = tmp.replace("?", "B", 1)
            else:
                tmp = tmp.replace("?", "C", 1)
        cnt = 0
        for j in range(len(tmp)-2):
            if tmp[j] == "A" and tmp[j+1] == "B" and tmp[j+2] == "C":
                cnt += 1
        ans += cnt
    print(ans % mod)

=======

def main():
    mod = 10 ** 9 + 7
    S = input()
    N = len(S)
    # 累積和を求める
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'A':
            A[i + 1] = A[i] + 1
            B[i + 1] = B[i]
            C[i + 1] = C[i]
        elif S[i] == 'B':
            A[i + 1] = A[i]
            B[i + 1] = B[i] + 1
            C[i + 1] = C[i]
        elif S[i] == 'C':
            A[i + 1] = A[i]
            B[i + 1] = B[i]
            C[i + 1] = C[i] + 1
        else:
            A[i + 1] = A[i]
            B[i + 1] = B[i]
            C[i + 1] = C[i]
    # 3^Qを求める
    Q = S.count('?')
    threeQ = pow(3, Q, mod)
    # A[i] * B[j] * C[k]を求める
    ABC = 0
    for i in range(N):
        if S[i] == '?':
            ABC += A[i] * B[N] - A[i] * B[i + 1]
            ABC += B[i] * C[N] - B[i] * C[i + 1]
            ABC += C[i] * A[N] - C[i] * A[i + 1]
        elif S[i] == 'A':
            ABC += B[i] * C[N] - B[i] * C[i + 1]
            ABC += C[i] * A[N] - C[i] * A[i + 1]
        elif S[i] == 'B':
            ABC += C[i] * A[N] - C[i] * A[i + 1]
            ABC += A[i] * B[N] - A[i] * B[i + 1]
        elif S[i] == 'C

=======

def main():
    import sys
    input = sys.stdin.readline
    mod = 10**9 + 7
    S = input().rstrip()
    Q = S.count("?")
    S = S.replace("?", "ABC")
    S = S.replace("A", "1")
    S = S.replace("B", "2")
    S = S.replace("C", "3")
    S = list(map(int, S))
    #print(S)
    L = len(S)
    dp = [[0] * 4 for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(L):
        #print(i)
        for j in range(4):
            if j == 0:
                dp[i + 1][j] = dp[i][j] * 3
            elif j == 1:
                dp[i + 1][j] = dp[i][j] * 2 + dp[i][j - 1]
            elif j == 2:
                dp[i + 1][j] = dp[i][j] * 2 + dp[i][j - 1]
            elif j == 3:
                dp[i + 1][j] = dp[i][j] * 1 + dp[i][j - 1]
            dp[i + 1][j] %= mod
    #print(dp)
    ans = 0
    for i in range(L):
        if S[i] == 1:
            ans += dp[L - i - 1][3]
        elif S[i] == 2:
            ans += dp[L - i - 1][2]
        elif S[i] == 3:
            ans += dp[L - i - 1][1]
        ans %= mod
    print(ans)
    return

=======

def main():
    S = input()
    Q = S.count("?")
    MOD = 10 ** 9 + 7
    # dp[i][j][k] := i文字目まで見て、Aがj個、Bがk個、Cがi-j-k個あるときのABC数
    dp = [[[0] * (Q + 1) for _ in range(Q + 1)] for _ in range(Q + 1)]
    dp[0][0][0] = 1
    for i in range(len(S)):
        if S[i] == "?":
            for j in range(Q + 1):
                for k in range(Q + 1):
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j + 1][k] += dp[i][j][k]
                    dp[i + 1][j][k + 1] += dp[i][j][k]
        elif S[i] == "A":
            for j in range(Q + 1):
                for k in range(Q + 1):
                    dp[i + 1][j + 1][k] += dp[i][j][k]
        elif S[i] == "B":
            for j in range(Q + 1):
                for k in range(Q + 1):
                    dp[i + 1][j][k + 1] += dp[i][j][k]
        else:
            for j in range(Q + 1):
                for k in range(Q + 1):
                    dp[i + 1][j][k] += dp[i][j][k]
    ans = 0
    for i in range(Q + 1):
        for j in range(Q + 1):
            ans += dp[len(S)][i][j]
    print(ans % MOD)

=======

def main():
    s = input()
    mod = 10**9 + 7
    q = s.count("?")
    # ?をA,B,Cのいずれかに置き換える通り数
    # 3^Q
    q = pow(3, q, mod)
    # A,B,Cの個数
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    # A,B,Cの個数の合計
    abc = a + b + c
    # A,B,Cの個数の合計の階乗
    # n! = n * (n-1) * (n-2) * ... * 1
    # 0! = 1
    # 1! = 1
    # 2! = 2
    # 3! = 6
    # 4! = 24
    # 5! = 120
    # 6! = 720
    # 7! = 5040
    # 8! = 40320
    # 9! = 362880
    # 10! = 3628800
    # 11! = 39916800
    # 12! = 479001600
    # 13! = 6227020800
    # 14! = 87178291200
    # 15! = 1307674368000
    # 16! = 20922789888000
    # 17! = 355687428096000
    # 18! = 6402373705728000
    # 19! = 121645100408832000
    # 20! = 2432902008176640000
    # 21! = 51090942171709440000
    # 22! = 1124000727777607680000
    # 23! = 25852016738884976640000
    # 24! = 620448401733239439360000
    # 25! = 15511210043330985984000000
    # 26! = 403291461126605635584000000
    # 27! =

=======

def main():
    from sys import stdin
    from collections import defaultdict
    from itertools import accumulate
    from operator import add
    from math import factorial
    readline = stdin.readline

    mod = 10**9 + 7
    N = len(readline().rstrip())
    dp = [defaultdict(int) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        c = readline().rstrip()[i]
        if c == '?':
            for j in range(N):
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * 3) % mod
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
        else:
            for j in range(N):
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % mod
    ans = 0
    for j in range(N + 1):
        ans = (ans + dp[N][j] * factorial(j) * pow(3, N - j, mod)) % mod
    print(ans)
