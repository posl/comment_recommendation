Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = S.count('?')

    # 1. 确定S中的C的位置
    cs = []
    for i in range(len(S)):
        if S[i] == 'C':
            cs.append(i)

    # 2. 确定S中的B的位置
    bs = []
    for c in cs:
        bs.append(S[:c].count('B'))

    # 3. 确定S中的A的位置
    ans = 0
    for b in bs:
        ans += S[:b].count('A')

    # 4. 计算答案
    for c in cs:
        ans += S[c:].count('A') * S[c:].count('B')

    # 5. 计算答案
    for q in range(Q):
        ans *= 3

    # 6. 打印答案
    print(ans % (10**9 + 7))

=======
Suggestion 2

def main():
    s = input()
    q = s.count("?")
    abc = 0
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == "A":
            abc += b * (3 ** q)
            abc %= 1000000007
            a += (3 ** q)
            a %= 1000000007
        elif s[i] == "B":
            b += a
            b %= 1000000007
        elif s[i] == "C":
            pass
        else:
            abc *= 3
            abc %= 1000000007
            b *= 3
            b %= 1000000007
            a *= 3
            a %= 1000000007
            q -= 1
    print(abc)

=======
Suggestion 3

def main():
    S = input()
    Q = S.count('?')
    A = 0
    B = 0
    C = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
    print((A*B*C)%1000000007)

=======
Suggestion 4

def main():
    s = input()
    q = s.count("?")
    ans = 1
    for i in range(1,q+1):
        ans *= 3
        ans %= 1000000007
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    Q = S.count('?')
    MOD = 10 ** 9 + 7
    S = S.replace('?', '0')
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            ans += pow(3, Q, MOD)
        elif S[i] == 'B':
            ans += pow(3, Q, MOD) * pow(2, i, MOD)
        elif S[i] == 'C':
            ans += pow(3, Q, MOD) * pow(2, i, MOD) * pow(2, len(S) - i - 1, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 6

def solve():
    s = input()
    q = s.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(q+1):
        ans += 3**i * 3**(q-i) * (q-i+1) * (q-i) // 2
        ans %= mod
    print(ans)

solve()

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    q = s.count("?")
    ans = 0
    for i in range(n):
        if s[i] == "B" or s[i] == "?":
            ans += pow(3, q, mod) * pow(3, i, mod)
            q -= 1
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(n):
        a[i + 1] = a[i] + (s[i] == 'A')
        b[i + 1] = b[i] + (s[i] == 'B')
        c[i + 1] = c[i] + (s[i] == 'C')
    ans = 0
    q = 0
    for i in range(n):
        if s[i] == 'A':
            ans += b[n] - b[i + 1]
            ans += c[n] - c[i + 1]
            ans += q
        elif s[i] == 'B':
            ans += a[n] - a[i + 1]
            ans += c[n] - c[i + 1]
            q += 1
        elif s[i] == 'C':
            ans += a[n] - a[i + 1]
            ans += b[n] - b[i + 1]
    for i in range(n):
        if s[i] == '?':
            ans = (ans * 3 + q) % mod
            q = q * 3 % mod
    print(ans % mod)

=======
Suggestion 9

def main():
    s = input()
    q = s.count('?')
    ans = 0
    mod = 10**9+7
    for i in range(len(s)):
        if s[i] == 'B' or s[i] == '?':
            ans += pow(3,q,mod) * pow(3,i,mod)
            q -= 1
        if s[i] == 'C' or s[i] == '?':
            ans += pow(3,q,mod) * pow(3,i,mod)
            q -= 1
    print(ans%mod)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    q = s.count('?')
    mod = 10**9 + 7
    ans = 0
    for i in range(n-2):
        if s[i] == 'A' or s[i] == '?':
            a = 3**q % mod
            b = 3**(q-1) % mod
            c = 3**(q-1) % mod
            ans += a+b+c
            ans %= mod
        if s[i] == 'B' or s[i] == '?':
            a = 3**q % mod
            b = 3**(q-1) % mod
            c = 3**(q-1) % mod
            ans += a+b+c
            ans %= mod
        if s[i] == 'C' or s[i] == '?':
            a = 3**q % mod
            b = 3**(q-1) % mod
            c = 3**(q-1) % mod
            ans += a+b+c
            ans %= mod
        if s[i] == '?':
            q -= 1
    print(ans)
