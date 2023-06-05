Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = S.count("?")
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    ans = 0
    for i in range(Q+1):
        for j in range(Q+1-i):
            k = Q-i-j
            ans += (pow(3,i,1000000007)*pow(3,j,1000000007)*pow(3,k,1000000007)*comb(A+i-1,i)*comb(B+j-1,j))%1000000007
    print(ans%1000000007)

=======
Suggestion 2

def main():
    s = input()
    #print(s)
    q = s.count('?')
    #print(q)
    #print(3**q)
    abc = 0
    for i in range(0, q+1):
        abc += 3**i * s.count('B?C') * 2**s.count('A?C') * 2**s.count('A?B') * 2**s.count('??A') * 2**s.count('??B') * 2**s.count('??C')
        abc += 3**i * s.count('A?B') * 2**s.count('B?C') * 2**s.count('A?C') * 2**s.count('??A') * 2**s.count('??B') * 2**s.count('??C')
        abc += 3**i * s.count('A?C') * 2**s.count('B?C') * 2**s.count('A?B') * 2**s.count('??A') * 2**s.count('??B') * 2**s.count('??C')
        abc %= 10**9 + 7
    print(abc)

=======
Suggestion 3

def main():
    s = input()
    t = s.replace('?', 'A')
    q = s.count('?')
    ans = 0
    for i in range(q+1):
        for j in range(q+1-i):
            k = q - i - j
            tmp = t
            tmp = tmp.replace('A', 'B', i)
            tmp = tmp.replace('B', 'C', j)
            tmp = tmp.replace('C', 'A', k)
            ans += tmp.count('ABC')
    print(ans % (10**9+7))

=======
Suggestion 4

def main():
    S = input()
    Q = S.count('?')
    mod = 10**9 + 7
    ans = 0
    for i, s in enumerate(S):
        if s == 'A':
            a = pow(3, Q, mod)
            b = pow(3, i, mod)
            ans += a * b
            ans %= mod
        elif s == 'B':
            a = pow(3, Q, mod)
            b = pow(3, i, mod)
            ans += a * b
            ans %= mod
            ans += pow(3, Q, mod)
            ans %= mod
        elif s == 'C':
            a = pow(3, Q, mod)
            b = pow(3, i, mod)
            ans += a * b
            ans %= mod
            ans += pow(3, Q, mod)
            ans %= mod
            ans += pow(3, Q, mod)
            ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    Q = S.count('?')
    mod = 10**9 + 7
    ans = 0
    for i in range(len(S)):
        if S[i] == 'B' or S[i] == '?':
            ans += pow(3, Q, mod) * pow(3, i, mod)
            ans %= mod
        if S[i] == 'C' or S[i] == '?':
            ans += pow(3, Q, mod) * pow(3, i, mod)
            ans %= mod
        Q -= 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    q = s.count('?')
    mod = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
    for i in range(len(s)):
        if s[i] == 'A':
            a -= 1
        elif s[i] == 'B':
            b -= 1
        elif s[i] == 'C':
            c -= 1
        elif s[i] == '?':
            ans += (a * pow(3, q, mod) + b * pow(3, q-1, mod) + c * pow(3, q-1, mod)) % mod
            q -= 1
    print(ans % mod)

=======
Suggestion 7

def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    ABC = 0

    # 3^Q 通りの文字列を作る
    for i in range(3**Q):
        # 3進数表現
        s = ''
        for j in range(Q):
            s += 'ABC'[(i // 3**j) % 3]

        # S の ? を置き換える
        j = 0
        for c in S:
            if c == '?':
                s = s[:j] + s[j+1:]
            j += 1

        # ABC の数を数える
        for j in range(len(s)):
            if s[j:j+3] == 'ABC':
                ABC += 1

    print(ABC % MOD)

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    ans = 0
    a = 0
    ab = 0
    abc = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            ab += a
        elif s[i] == 'C':
            abc += ab
        else:
            abc = 3*abc + ab
            ab = 3*ab + a
            a = 3*a + 1
    ans = abc % mod
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    q = s.count('?')
    p = 1
    for i in range(1,q+1):
        p = (p*3)%1000000007
    ans = 0
    c = 0
    for i in s:
        if i == 'C':
            c += 1
        elif i == 'B':
            ans += c*p
        elif i == '?':
            ans += c*p
            c = (c*2)%1000000007
    print(ans%1000000007)

=======
Suggestion 10

def main():
    s = input()
    q = s.count("?")
    mod = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += 1
        elif s[i] == "C":
            c += 1
    for i in range(len(s)):
        if s[i] == "B" or s[i] == "?":
            ans += a * c * pow(3, q, mod)
            if s[i] == "?":
                q -= 1
        if s[i] == "A":
            a -= 1
        if s[i] == "C":
            c -= 1
    print(ans % mod)
