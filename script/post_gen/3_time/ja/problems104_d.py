Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = s.count("?")
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    ans = 0
    for i in range(len(s)):
        if s[i] == "A":
            a -= 1
        elif s[i] == "B":
            b -= 1
        elif s[i] == "C":
            c -= 1
        elif s[i] == "?":
            q -= 1
            ans += (a*pow(3,q,10**9+7)+b*pow(3,q,10**9+7)+c*pow(3,q,10**9+7))
            ans %= 10**9+7
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    a = [0]*n
    b = [0]*n
    c = [0]*n
    q = [0]*n
    for i in range(n):
        if s[i] == 'A':
            a[i] += 1
        elif s[i] == 'B':
            b[i] += 1
        elif s[i] == 'C':
            c[i] += 1
        elif s[i] == '?':
            q[i] += 1
        if i > 0:
            a[i] += a[i-1]
            b[i] += b[i-1]
            c[i] += c[i-1]
            q[i] += q[i-1]
    ans = 0
    mod = 10**9+7
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            ans += a[i]*(pow(3, q[i], mod))%mod
            ans %= mod
            ans += c[i]*(pow(3, q[i], mod))%mod
            ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    a = []
    b = []
    c = []
    q = 0
    for i in range(n):
        if s[i] == 'A':
            a.append(i)
        elif s[i] == 'B':
            b.append(i)
        elif s[i] == 'C':
            c.append(i)
        else:
            q += 1
    ans = 0
    for i in range(len(b)):
        ans += len(a) * (len(c) + len(b) + len(c) - b[i])
    print(ans % (10**9+7))

=======
Suggestion 4

def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')

    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A -= 1
        elif S[i] == 'B':
            B -= 1
        elif S[i] == 'C':
            C -= 1
        elif S[i] == '?':
            Q -= 1
            ans += (pow(3, Q, MOD) * (A * pow(3, B, MOD) + B * pow(3, C, MOD) + C * pow(3, A, MOD))) % MOD
            ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    Q = S.count("?")
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(N):
        if S[i] == "A":
            a = 1
        elif S[i] == "B":
            a = 2
        elif S[i] == "C":
            a = 3
        else:
            a = 0
        if a > 0:
            ans += a * pow(3, Q, MOD) * pow(3, i, MOD)
            ans %= MOD
        Q -= 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    q = s.count("?")
    MOD = 10**9 + 7
    ans = 0
    for i in range(n):
        if s[i] == "A":
            a = 1
        elif s[i] == "B":
            a = 2
        elif s[i] == "C":
            a = 3
        else:
            a = 0
        if a != 0:
            ans += a * pow(3, q, MOD) * pow(3, i, MOD)
            ans %= MOD
            q -= 1
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    Q = S.count('?')
    Q3 = pow(3, Q, 10**9+7)
    A = [0] * len(S)
    B = [0] * len(S)
    C = [0] * len(S)
    for i, s in enumerate(S):
        if s == 'A':
            A[i] = 1
        elif s == 'B':
            B[i] = 1
        elif s == 'C':
            C[i] = 1
    for i in range(1, len(S)):
        A[i] += A[i-1]
        B[i] += B[i-1]
        C[i] += C[i-1]
    ans = 0
    for i, s in enumerate(S):
        if s == '?':
            ans += A[i-1] * B[i-1] * (Q3 // 3) % (10**9+7)
            ans += A[i-1] * C[i-1] * (Q3 // 3) % (10**9+7)
            ans += B[i-1] * C[i-1] * (Q3 // 3) % (10**9+7)
            ans %= 10**9+7
    print(ans)

main()

=======
Suggestion 8

def main():
    S = input()
    n = len(S)
    MOD = 10**9+7
    ans = 0
    cnt = 0
    for i in range(n):
        if S[i] == 'A':
            ans += pow(3,cnt,MOD)
        elif S[i] == '?':
            ans += pow(3,cnt+1,MOD)
            cnt += 1
    print(ans%MOD)

=======
Suggestion 9

def main():
    S = input()
    Q = S.count('?')
    S = S.replace('?','{}')
    S = S.format('A','B','C')
    S = S.replace('{}','?')
    S = S.replace('A','0')
    S = S.replace('B','1')
    S = S.replace('C','2')
    S = S.replace('?','3')
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if S[i] == '3':
            ans += pow(3,i,Q)
    ans = ans % (10**9+7)
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    Q = S.count('?')
    print(Q)
    print(S)
    print(3**Q)
    #print(3**Q%1000000007)
