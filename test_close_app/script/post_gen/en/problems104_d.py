Synthesizing 10/10 solutions

=======

def main():
    MOD = 10 ** 9 + 7
    S = input()
    N = len(S)
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i, s in enumerate(S, 1):
        for j in range(4):
            if s == "?":
                dp[i][j] += 3 * dp[i - 1][j]
            else:
                dp[i][j] += dp[i - 1][j]
            if j > 0 and (s == j or s == "?"):
                dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD
    print(dp[-1][-1])

=======

def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    dp = [[0]*3 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3):
            if s[i] == "?":
                dp[i+1][j] += dp[i][j]*3
                dp[i+1][(j+1)%3] += dp[i][j]
            else:
                if s[i] == "ABC"[j]:
                    dp[i+1][(j+1)%3] += dp[i][j]
        for j in range(3):
            dp[i+1][j] %= mod
    print(dp[n][0])

=======

def main():
    S = input()
    MOD = 10 ** 9 + 7
    Q = S.count("?")
    A, B, C = S.count("A"), S.count("B"), S.count("C")
    ans = 0
    for i in range(Q):
        ans = (ans * 3 + pow(3, Q - i - 1, MOD) * (A + B + C)) % MOD
        A, B, C = (A * 2 + pow(3, i, MOD) * A) % MOD, (B * 2 + pow(3, i, MOD) * B) % MOD, (C * 2 + pow(3, i, MOD) * C) % MOD
    print(ans)

=======

def main():
    S = input()
    MOD = 10**9 + 7
    N = len(S)
    Q = S.count("?")
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            if S[i] == "?" or S[i] == "ABC"[j]:
                dp[i + 1][j] += dp[i][j] * 3**(Q - 1)
            if S[i] == "?":
                dp[i + 1][j] += dp[i][j] * 3**(Q - 2)
            if j > 0 and (S[i] == "?" or S[i] == "ABC"[j - 1]):
                dp[i + 1][j] += dp[i][j - 1]
            dp[i + 1][j] %= MOD
    print(dp[N][3])

=======

def main():
    s = input()
    abc = [0, 0, 0]
    ans = 0
    mod = 1000000007
    for i in range(len(s)):
        if s[i] == '?':
            ans = ans * 3 + abc[0] + abc[1] + abc[2]
        elif s[i] == 'A':
            ans = ans * 3 + abc[0]
            abc[0] += 1
        elif s[i] == 'B':
            ans = ans * 3 + abc[1]
            abc[1] += 1
        elif s[i] == 'C':
            ans = ans * 3 + abc[2]
            abc[2] += 1
        ans %= mod
    print(ans)

=======

def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(n):
        if s[i] == '?':
            ans += 3 ** (n - i - 1)
            ans %= mod
    abc = [0, 0, 0]
    for i in range(n):
        if s[i] == '?':
            abc[0] = (abc[0] * 3 + 1) % mod
            abc[1] = (abc[1] * 3 + abc[0]) % mod
            abc[2] = (abc[2] * 3 + abc[1]) % mod
        else:
            abc[ord(s[i]) - ord('A')] = (abc[ord(s[i]) - ord('A')] * 3 + abc[ord(s[i]) - ord('A') - 1]) % mod
    ans += abc[2]
    ans %= mod
    print(ans)

=======

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    # dp[i][j][k] := i?

=======

def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7

    # dp[i][j]: i文字目まで見て、Aがj個、Bがi-j個のときのパターン数
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N+1):
            if S[i] == 'A':
                dp[i+1][j] = dp[i][j]
            elif S[i] == 'B':
                dp[i+1][j] = dp[i][j] * j % MOD
            elif S[i] == 'C':
                dp[i+1][j] = dp[i][j] * j * (j-1) // 2 % MOD
            else:
                dp[i+1][j] = dp[i][j] * 3 % MOD
                if j > 0:
                    dp[i+1][j] += dp[i][j-1] * j % MOD
                if j > 1:
                    dp[i+1][j] += dp[i][j-1] * j * (j-1) // 2 % MOD
                dp[i+1][j] %= MOD

    print(dp[N][N-1])

=======

def abc_number(s):
    # 3^Q strings
    # A = 65, B = 66, C = 67
    # ? = 63
    # A = 0, B = 1, C = 2
    # 0 = A, 1 = B, 2 = C
    # 3^Q = 3^(Q-A) * 3^A
    # 3^(Q-A) * 3^A = 3^(Q-A) * 3^Q / 3^Q
    # 3^(Q-A) * 3^Q / 3^Q = 3^(Q-A)
    # 3^(Q-A) = 3^(Q-A) * 3^Q / 3^Q
    # 3^(Q-A) = 3^Q
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-63)
    # 3^(Q-A) = 3^(Q-63) * 3^63 / 3^63
    # 3^(Q-A) = 3^(Q-

=======

def abc_number(s):
    # Replace this with your code
    return 0
