Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            if S[i] == "?":
                dp[i + 1][j] += dp[i][j] * 3
                dp[i + 1][j] %= MOD
                if j < 3:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= MOD
            else:
                if j < 3 and S[i] == "ABC"[j]:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= MOD
    print(dp[N][3])

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    dp = [[0]*4 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        if s[i] == 'A':
            dp[i+1][0] = (dp[i][0]*3+dp[i][1])%mod
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = dp[i][2]
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
        elif s[i] == 'B':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = (dp[i][0]+dp[i][1]*3)%mod
            dp[i+1][2] = dp[i][2]
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
        elif s[i] == 'C':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = (dp[i][0]+dp[i][2]*3)%mod
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
        else:
            dp[i+1][0] = (dp[i][0]*3+dp[i][1])%mod
            dp[i+1][1] = (dp[i][0]+dp[i][1]*3)%mod
            dp[i+1][2] = (dp[i][0]+dp[i][2]*3)%mod
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
    print(dp[n][3])

=======
Suggestion 3

def main():
    s = input()
    mod = 10**9 + 7
    n = len(s)
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            if s[i] == "?":
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * 3) % mod
            else:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            if j < 3 and (s[i] == "?" or s[i] == "ABC"[j]):
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % mod
    print(dp[n][3])

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if S[i] == '?':
                    for l in range(3):
                        dp[i + 1][j][k] += dp[i][j][k]
                        dp[i + 1][j][k] %= MOD
                        dp[i + 1][l][j] += dp[i][j][k]
                        dp[i + 1][l][j] %= MOD
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= MOD
                    dp[i + 1][int(S[i])][j] += dp[i][j][k]
                    dp[i + 1][int(S[i])][j] %= MOD
    print(dp[N][3][3])

main()

=======
Suggestion 5

def main():
    S = input()
    ABC = [0, 0, 0]
    ABC[0] = S.count('A')
    ABC[1] = S.count('B')
    ABC[2] = S.count('C')
    Q = S.count('?')
    mod = 10**9 + 7

    #print(ABC, Q)
    dp = [[0] * 4 for _ in range(Q+1)]
    dp[0][3] = 1

    #print(dp)
    for i in range(Q):
        for j in range(4):
            dp[i+1][j] = dp[i][j] * 2
            dp[i+1][j] %= mod

        for j in range(3):
            dp[i+1][j] += dp[i][3]
            dp[i+1][j] %= mod

        dp[i+1][3] += dp[i][3]
        dp[i+1][3] %= mod

    #print(dp)

    ans = 0
    for i in range(3):
        ans += dp[Q][i] * ABC[i]
        ans %= mod

    ans += dp[Q][3]
    ans %= mod

    print(ans)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    A = 0
    B = 0
    C = 0
    Q = 0
    for i in range(N):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
        else:
            Q += 1
    ABC = A * B * C
    ABC2 = ABC * pow(3, Q, MOD) % MOD
    ABC3 = ABC2 * pow(3, MOD - 2, MOD) % MOD
    ABC4 = ABC3 * pow(3, MOD - 2, MOD) % MOD
    ABC5 = ABC4 * pow(3, MOD - 2, MOD) % MOD
    ABC6 = ABC5 * pow(3, MOD - 2, MOD) % MOD
    ABC7 = ABC6 * pow(3, MOD - 2, MOD) % MOD
    ABC8 = ABC7 * pow(3, MOD - 2, MOD) % MOD
    ABC9 = ABC8 * pow(3, MOD - 2, MOD) % MOD
    ABC10 = ABC9 * pow(3, MOD - 2, MOD) % MOD
    ABC11 = ABC10 * pow(3, MOD - 2, MOD) % MOD
    ABC12 = ABC11 * pow(3, MOD - 2, MOD) % MOD
    ABC13 = ABC12 * pow(3, MOD - 2, MOD) % MOD
    ABC14 = ABC13 * pow(3, MOD - 2, MOD) % MOD
    ABC15 = ABC14 * pow(3, MOD - 2, MOD) % MOD
    ABC16 = ABC15 * pow(3, MOD - 2, MOD) % MOD
    ABC17 = ABC16 * pow(3, MOD - 2, MOD) % MOD
    ABC18 = ABC17 * pow(3, MOD - 2, MOD) % MOD
    ABC19 = ABC18 * pow(3, MOD - 2, MOD) % MOD
    ABC20 = ABC19 * pow

=======
Suggestion 7

def solve():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    dp = [[[0]*3 for _ in range(3)] for _ in range(N)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if j == k == 0:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][0] += dp[i][0][0]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][0][0]
                    if S[i] == 'C' or S[i] == '?':
                        dp[i+1][0][0] += dp[i][0][0]
                elif j == 1 and k == 0:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][0] += dp[i][1][0]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][1][0]
                    if S[i] == 'C' or S[i] == '?':
                        dp[i+1][0][0] += dp[i][1][0]
                elif j == 0 and k == 1:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][1] += dp[i][0][1]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][0][1]
                    if S[i] == 'C' or S[i] == '?':
                        dp[i+1][0][0] += dp[i][0][1]
                elif j == 1 and k == 1:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][1] += dp[i][1][1]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][1][1]

=======
Suggestion 8

def abcnum(s):
    a = 0
    b = 0
    c = 0
    abc = 0
    q = 0
    for i in s:
        if i == 'A':
            a += 1
        elif i == 'B':
            b += 1
        elif i == 'C':
            c += 1
        elif i == '?':
            q += 1
    abc += a * b * q + a * c * b + b * c * a
    return (abc % (10**9 + 7))

s = input()
print(abcnum(s))

=======
Suggestion 9

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    pow3Q = pow(3, Q, MOD)
    ans = 0
    for i in range(pow3Q):
        T = S
        for j in range(Q):
            if i >> j & 1:
                T = T.replace('?', 'A', 1)
            elif i >> j & 2:
                T = T.replace('?', 'B', 1)
            else:
                T = T.replace('?', 'C', 1)
        ans = (ans + ABCnumber(T)) % MOD
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    Q = S.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(3**Q):
        tmp = ''
        for j in range(Q):
            if i%(3**(j+1))//(3**j) == 0:
                tmp += 'A'
            elif i%(3**(j+1))//(3**j) == 1:
                tmp += 'B'
            else:
                tmp += 'C'
        tmp = tmp[::-1]
        cnt = 0
        for j in range(len(S)):
            if S[j] == '?':
                S = S[:j] + tmp[cnt] + S[j+1:]
                cnt += 1
        cnt = 0
        for j in range(len(S)-2):
            if S[j] == 'A' and S[j+1] == 'B' and S[j+2] == 'C':
                cnt += 1
        ans += cnt
    print(ans%mod)
