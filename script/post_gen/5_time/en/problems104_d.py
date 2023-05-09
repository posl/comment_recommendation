Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = s.replace('?', '0')
    s = s.replace('A', '1')
    s = s.replace('B', '2')
    s = s.replace('C', '3')
    s = s.replace('0', 'ABC')
    s = s.replace('1', 'AB')
    s = s.replace('2', 'BC')
    s = s.replace('3', 'AC')
    s = list(s)
    s = list(map(int, s))
    MOD = 10**9 + 7
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 1 or s[i] == 2 or s[i] == 3:
            cnt += 1
        elif s[i] == 0:
            ans += cnt
        else:
            ans += cnt
            cnt = 0
    print(ans % MOD)
main()

=======
Suggestion 2

def main():
    s = input()
    n = len(s)

    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)

    for i in range(n):
        a[i + 1] = a[i]
        b[i + 1] = b[i]
        c[i + 1] = c[i]
        if s[i] == "A":
            a[i + 1] += pow(3, s[:i].count("?"), 10 ** 9 + 7)
        elif s[i] == "B":
            b[i + 1] += pow(3, s[:i].count("?"), 10 ** 9 + 7)
        elif s[i] == "C":
            c[i + 1] += pow(3, s[:i].count("?"), 10 ** 9 + 7)
        else:
            a[i + 1] += 2 * pow(3, s[:i].count("?"), 10 ** 9 + 7)
            b[i + 1] += 2 * pow(3, s[:i].count("?"), 10 ** 9 + 7)
            c[i + 1] += 2 * pow(3, s[:i].count("?"), 10 ** 9 + 7)

    ans = 0
    for i in range(n):
        if s[i] == "B" or s[i] == "?":
            ans += a[i] * c[n] % (10 ** 9 + 7)
        if s[i] == "A" or s[i] == "?":
            ans += b[i] * c[n] % (10 ** 9 + 7)
        if s[i] == "?":
            ans += b[i] * c[n] % (10 ** 9 + 7)
            ans += a[i] * c[n] % (10 ** 9 + 7)
            ans += b[i] * a[n] % (10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    A = 0
    B = 0
    C = 0
    Q = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
        else:
            Q += 1
    abc = 0
    for i in range(Q):
        abc += pow(3,i,1000000007) * (pow(3,Q-i-1,1000000007) * A * B * C % 1000000007 + pow(3,Q-i-1,1000000007) * A * B % 1000000007 + pow(3,Q-i-1,1000000007) * B * C % 1000000007 + pow(3,Q-i-1,1000000007) * C * A % 1000000007 + pow(3,Q-i-1,1000000007) * A % 1000000007 + pow(3,Q-i-1,1000000007) * B % 1000000007 + pow(3,Q-i-1,1000000007) * C % 1000000007 + pow(3,Q-i-1,1000000007) % 1000000007)
        abc %= 1000000007
    print(abc)

=======
Suggestion 4

def main():
    S = input()
    Q = S.count('?')
    A = [0] * (Q + 1)
    B = [0] * (Q + 1)
    C = [0] * (Q + 1)
    for i, c in enumerate(S):
        if c == 'A':
            A[Q - i] += 1
        elif c == 'B':
            B[Q - i] += 1
        elif c == 'C':
            C[Q - i] += 1
        elif c == '?':
            A[Q - i] += 1
            B[Q - i] += 1
            C[Q - i] += 1
        A[Q - i - 1] += A[Q - i]
        B[Q - i - 1] += B[Q - i]
        C[Q - i - 1] += C[Q - i]
    ans = 0
    for i in range(Q + 1):
        ans += A[i] * B[i] * C[i]
        ans %= 10**9 + 7
    print(ans)

main()

=======
Suggestion 5

def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    mod = 10**9 + 7
    ans = 0
    for i in range(Q+1):
        for j in range(Q+1):
            if i + j > Q:
                continue
            k = Q - i - j
            t = 1
            for _ in range(i):
                t = t * (A + _ + 1) % mod
            for _ in range(j):
                t = t * (B + _ + 1) % mod
            for _ in range(k):
                t = t * (C + _ + 1) % mod
            ans = (ans + t) % mod
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    q = s.count('?')
    mod = 10**9 + 7
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == 'A':
            a += pow(3, q, mod)
        elif s[i] == 'B':
            b += pow(3, q, mod)
        elif s[i] == 'C':
            c += pow(3, q, mod)
        else:
            a, b, c = (a*3 + pow(3, q-1, mod)) % mod, (b*3 + a) % mod, (c*3 + b) % mod
    print(c%mod)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    MOD = 10 ** 9 + 7
    dp = [[0]*4 for i in range(n+1)]
    dp[n][3] = 1
    for i in range(n-1, -1, -1):
        for j in range(4):
            if s[i] == '?':
                dp[i][j] = 3 * dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j]
            if j < 3 and (s[i] == '?' or s[i] == 'ABC'[j]):
                dp[i][j] += dp[i+1][j+1]
            dp[i][j] %= MOD
    print(dp[0][0])

=======
Suggestion 8

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    dp = [1]
    for i in range(Q):
        dp.append(dp[-1] * 3 % MOD)
    ans = 0
    cnt = 0
    for i, s in enumerate(S):
        if s == 'A':
            cnt += dp[i]
        elif s == 'B':
            ans += cnt * dp[Q - i]
        elif s == 'C':
            ans += cnt * dp[Q - i] * dp[Q - i]
    print(ans % MOD)

=======
Suggestion 9

def getABCNumber(s):
    abc = 0
    q = 0
    for i in range(len(s)):
        if s[i] == 'A':
            abc += q
        elif s[i] == 'B':
            q += abc
        elif s[i] == 'C':
            q = q
        else:
            abc = abc * 3 + q
            q = q * 3
        abc %= 1000000007
        q %= 1000000007
    return abc

s = input()
print(getABCNumber(s))

=======
Suggestion 10

def main():
    S = input()
    MOD = 10**9 + 7

    # 1. ?をA, B, Cに置換した文字列を作る
    # 2. ABCの数を数える
    # 3. 1と2を繰り返す
    # 4. 答えを出力する

    # 1
    S = S.replace('?', 'D')

    # 2
    count = 0
    ABC_count = 0
    for i in range(len(S)):
        if S[i] == 'A':
            count += 1
        elif S[i] == 'B':
            ABC_count += count
        elif S[i] == 'C':
            ABC_count = (ABC_count * 3 + count) % MOD
        else:
            ABC_count = (ABC_count * 3 + count * 3) % MOD
            count = (count * 3) % MOD

    # 3
    print(ABC_count)
