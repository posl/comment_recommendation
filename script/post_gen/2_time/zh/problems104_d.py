Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = S.count("?")
    mod = int(1e9+7)
    count = 0
    for i in range(3**Q):
        T = S
        for j in range(Q):
            T = T.replace("?", "ABC"[i//3**j%3], 1)
        count += T.count("ABC")
    print(count%mod)

=======
Suggestion 2

def solve(s):
    modulo = 10**9 + 7
    q = s.count('?')
    if q == 0:
        return countABC(s)
    res = 0
    for i in range(3**q):
        res += countABC(s.replace('?', 'A', i))
        res %= modulo
    return res

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    dp = [0]*8
    dp[0] = 1
    for i in range(n):
        if s[i] == 'A':
            dp[1] = (dp[1]+dp[0])%mod
        elif s[i] == 'B':
            dp[2] = (dp[2]+dp[1])%mod
        elif s[i] == 'C':
            dp[3] = (dp[3]+dp[2])%mod
        elif s[i] == '?':
            dp[3] = (dp[3]*3+dp[2])%mod
            dp[2] = (dp[2]*3+dp[1])%mod
            dp[1] = (dp[1]*3+dp[0])%mod
            dp[0] = dp[0]*3%mod
    print(dp[3])

=======
Suggestion 4

def main():
    S = input()
    Q = S.count('?')
    cnt = 0
    for i in range(len(S)):
        if S[i] == 'A':
            cnt += pow(3, Q, 10**9 + 7)
        elif S[i] == 'B':
            cnt += pow(3, Q, 10**9 + 7) * 2
        elif S[i] == 'C':
            cnt += pow(3, Q, 10**9 + 7) * 4
        else:
            cnt += pow(3, Q - 1, 10**9 + 7)
            if i < len(S) - 1:
                if S[i + 1] == 'A':
                    cnt += pow(3, Q - 1, 10**9 + 7)
                elif S[i + 1] == 'B':
                    cnt += pow(3, Q - 1, 10**9 + 7) * 2
                elif S[i + 1] == 'C':
                    cnt += pow(3, Q - 1, 10**9 + 7) * 4
            if i < len(S) - 2:
                if S[i + 2] == 'A':
                    cnt += pow(3, Q - 2, 10**9 + 7)
                elif S[i + 2] == 'B':
                    cnt += pow(3, Q - 2, 10**9 + 7) * 2
                elif S[i + 2] == 'C':
                    cnt += pow(3, Q - 2, 10**9 + 7) * 4
    print(cnt % (10**9 + 7))

=======
Suggestion 5

def main():
    s = input()
    q = s.count('?')

    # calculate a, b, c
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')

    # calculate 3^q
    ans = pow(3, q, 10**9+7)

    # calculate ans
    for i in range(q+1):
        for j in range(q+1-i):
            k = q - i - j
            tmp = pow(3, i, 10**9+7) * pow(3, j, 10**9+7) * pow(3, k, 10**9+7)
            tmp = tmp * a * b * c
            ans += tmp
            ans %= 10**9+7

    print(ans)

=======
Suggestion 6

def main():
    s = input()
    q = s.count('?')
    mod = 10**9+7
    l = len(s)
    ans = 0
    for i in range(l):
        if s[i] == 'C':
            ans += pow(3,q,mod)*pow(3,i,mod)
            ans %= mod
        elif s[i] == 'B':
            ans += pow(3,q,mod)*pow(3,i,mod)
            ans %= mod
            q -= 1
        elif s[i] == 'A':
            ans += pow(3,q,mod)*pow(3,i,mod)
            ans %= mod
            q -= 1
            q -= s[i+1:].count('?')
    print(ans)

=======
Suggestion 7

def solve(s):
    n = len(s)
    mod = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
        else:
            ans = (ans*3 + c)%mod
            ans = (ans*3 + b)%mod
            ans = (ans*3 + a)%mod
            a = (a*3)%mod
            b = (b*3)%mod
            c = (c*3)%mod
    return ans

=======
Suggestion 8

def solve():
    s = input()
    mod = 10**9 + 7
    a,b,c = 0,0,0
    for i in range(len(s)):
        if s[i] == 'A':
            a += pow(3,i,mod)
        elif s[i] == 'B':
            b += a
        elif s[i] == 'C':
            c += b
        else:
            c = 3*c + b
            b = 3*b + a
            a = 3*a + pow(3,i,mod)
        a %= mod
        b %= mod
        c %= mod
    print(c)

=======
Suggestion 9

def main():
    s = input()
    s = s.replace("?", "0")
    s = s.replace("A", "1")
    s = s.replace("B", "2")
    s = s.replace("C", "3")
    s = s.replace("0", "ABC")
    s = s.replace("1", "BC")
    s = s.replace("2", "AC")
    s = s.replace("3", "AB")
    print(s.count("ABC") % (10 ** 9 + 7))

=======
Suggestion 10

def solve():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    ans = 0
    power3 = 1
    for i in range(N-1, -1, -1):
        if S[i] == 'C':
            ans += power3
            ans %= MOD
        elif S[i] == '?':
            ans *= 3
            ans %= MOD
            power3 *= 3
            power3 %= MOD
        else:
            pass
    print(ans)

solve()
