Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9+7
    ans = 0
    for i in range(len(S)):
        if S[i] == 'C':
            ans += pow(3,Q,MOD)*pow(3,i,MOD)
            ans %= MOD
        elif S[i] == 'B':
            ans += pow(3,Q,MOD)*pow(3,i,MOD)
            ans %= MOD
            Q -= 1
        elif S[i] == 'A':
            ans += pow(3,Q,MOD)*pow(3,i,MOD)
            ans %= MOD
            Q -= 1
    print(ans)

main()

=======
Suggestion 2

def solve():
    S = input()
    Q = S.count("?")
    mod = 10**9 + 7
    dp = [[0 for _ in range(3)] for _ in range(3)]
    dp[0][0] = 1
    for i in range(len(S)):
        if S[i] == 'A':
            dp[1][0] += dp[0][0]
            dp[1][1] += dp[0][1]
            dp[1][2] += dp[0][2]
        elif S[i] == 'B':
            dp[2][0] += dp[1][0]
            dp[2][1] += dp[1][1]
            dp[2][2] += dp[1][2]
        elif S[i] == 'C':
            dp[0][0] += dp[2][0]
            dp[0][1] += dp[2][1]
            dp[0][2] += dp[2][2]
        else:
            dp[1][0] += dp[0][0]
            dp[1][1] += dp[0][1]
            dp[1][2] += dp[0][2]
            dp[2][0] += dp[1][0]
            dp[2][1] += dp[1][1]
            dp[2][2] += dp[1][2]
            dp[0][0] += dp[2][0]
            dp[0][1] += dp[2][1]
            dp[0][2] += dp[2][2]
        for j in range(3):
            dp[j][0] %= mod
            dp[j][1] %= mod
            dp[j][2] %= mod
    print(dp[0][2] % mod)

=======
Suggestion 3

def main():
    S = input()
    n = len(S)
    Q = S.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(n):
        if S[i] == 'B' or S[i] == '?':
            ans += pow(3,Q,mod)*pow(3,i,mod)*pow(2,n-1-i,mod)
            ans %= mod
        if S[i] == 'C' or S[i] == '?':
            ans += pow(3,Q,mod)*pow(3,i,mod)*pow(2,n-1-i,mod)
            ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    q = s.count('?')
    a = [0] * (q + 1)
    b = [0] * (q + 1)
    c = [0] * (q + 1)
    for i in range(q):
        a[i + 1] = a[i] * 3 + (s[i] == 'A')
        b[i + 1] = b[i] * 3 + (s[i] == 'B')
        c[i + 1] = c[i] * 3 + (s[i] == 'C')
    ans = 0
    for i in range(len(s)):
        if s[i] == 'B' or s[i] == '?':
            ans += a[q] * c[q] - a[q - 1] * c[q - 1]
            ans %= 1000000007
        if s[i] == 'A' or s[i] == '?':
            ans += b[q] * c[q] - b[q - 1] * c[q - 1]
            ans %= 1000000007
        if s[i] == '?':
            ans += b[q - 1] * c[q - 1] - a[q - 1] * c[q - 1]
            ans %= 1000000007
            ans += a[q - 1] * b[q - 1] - b[q - 1] * c[q - 1]
            ans %= 1000000007
            ans += a[q - 1] * c[q - 1] - a[q - 1] * b[q - 1]
            ans %= 1000000007
            q -= 1
    print(ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    S = input()
    S = S.replace("?", "0")
    S = S.replace("A", "1")
    S = S.replace("B", "2")
    S = S.replace("C", "3")
    Q = S.count("0")
    S = int(S)
    mod = 10**9 + 7
    ans = 3**Q
    for i in range(Q):
        ans = (ans * 3) % mod
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    c = [0] * n
    q = [0] * n
    for i in range(n):
        if s[i] == 'A':
            a[i] = 1
        elif s[i] == 'B':
            b[i] = 1
        elif s[i] == 'C':
            c[i] = 1
        else:
            q[i] = 1
    for i in range(1, n):
        a[i] += a[i-1]
        b[i] += b[i-1]
        c[i] += c[i-1]
        q[i] += q[i-1]
    ans = 0
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            for j in range(i+1, n):
                if s[j] == 'C' or s[j] == '?':
                    ans += a[i] * (q[j] - q[i])
                    ans %= 10**9+7
    print(ans)

=======
Suggestion 8

def solve():
    S = input()
    MOD = 10**9+7
    Q = S.count('?')
    N = len(S)
    # DP[i][j] = (S[i:]について, '?'をj個Aに置き換えたときのABC数)
    DP = [[0] * (Q+1) for _ in range(N+1)]
    DP[N][Q] = 1
    for i in range(N-1, -1, -1):
        for j in range(Q+1):
            if S[i] == 'C':
                DP[i][j] = DP[i+1][j]
            elif S[i] == 'B':
                DP[i][j] = DP[i+1][j+1]
            elif S[i] == 'A':
                DP[i][j] = DP[i+1][j+2]
            else:
                DP[i][j] = (3 * DP[i+1][j] + DP[i+1][j+1] + DP[i+1][j+2]) % MOD
    print(DP[0][0])

solve()

=======
Suggestion 9

def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    # print('Q=', Q)
    # print('A=', A)
    # print('B=', B)
    # print('C=', C)
    # print('S=', S)

    # print('3^Q=', 3**Q)
    # print('3^Q%1000000007=', 3**Q%1000000007)
    # print('3^Q%1000000007*Q=', 3**Q%1000000007*Q)
    # print('3^Q%1000000007*Q%1000000007=', 3**Q%1000000007*Q%1000000007)

    # print('3^Q%1000000007*A=', 3**Q%1000000007*A)
    # print('3^Q%1000000007*A%1000000007=', 3**Q%1000000007*A%1000000007)
    # print('3^Q%1000000007*A%1000000007*B=', 3**Q%1000000007*A%1000000007*B)
    # print('3^Q%1000000007*A%1000000007*B%1000000007=', 3**Q%1000000007*A%1000000007*B%1000000007)
    # print('3^Q%1000000007*A%1000000007*B%1000000007*C=', 3**Q%1000000007*A%1000000007*B%1000000007*C)
    # print('3^Q%1000000007*A%1000000007*B%1000000007*C%1000000007=', 3**Q%1000000007*A%1000000007*B%1000000007*C%1000000007)

    print((3**Q%1000000007*Q%1000000007+3**Q%1000000007*A%1000000007*B%1000000007+3**Q%1000000007*A%1000000007*C%1000000007)%1000000007)

=======
Suggestion 10

def main():
    S = input()
    #print(S)
    Q = S.count('?')
    #print(Q)
    len_S = len(S)
    #print(len_S)
    cnt = 0
    for i in range(len_S):
        if S[i] == 'A':
            cnt += (pow(3,Q) * pow(3,i)) % 1000000007
        elif S[i] == 'B':
            cnt += (pow(3,Q) * pow(3,i) * 2) % 1000000007
        elif S[i] == 'C':
            cnt += (pow(3,Q) * pow(3,i) * 4) % 1000000007
        else:
            cnt += (pow(3,Q) * pow(3,i) * 3) % 1000000007
    print(cnt % 1000000007)

main()
