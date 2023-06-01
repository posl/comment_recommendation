Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s=input()
    n=len(s)
    q=s.count("?")
    ans=0
    for i in range(n):
        if s[i]=="B" or s[i]=="?":
            ans+=pow(3,q,1000000007)*pow(3,i,1000000007)
            q-=1
        if s[i]=="C" or s[i]=="?":
            ans+=pow(3,q,1000000007)*pow(3,i,1000000007)
            q-=1
    print(ans%1000000007)

=======
Suggestion 2

def main():
    s = input()
    l = len(s)
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(l):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
    ans = (a * b * c) % 1000000007
    for i in range(l):
        if s[i] == '?':
            a -= 1
            ans = (ans + a * b * c) % 1000000007
        elif s[i] == 'A':
            a -= 1
        elif s[i] == 'B':
            b -= 1
        elif s[i] == 'C':
            c -= 1
    print(ans)

=======
Suggestion 3

def problem104_d():
    pass

=======
Suggestion 4

def main():
    s = input()
    len_s = len(s)
    q = s.count('?')
    mod = 10**9+7
    a = 0
    b = 0
    c = 0
    for i in range(len_s):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
    ans = 0
    for i in range(q+1):
        for j in range(q-i+1):
            k = q-i-j
            ans += pow(3,i,mod)*pow(3,j,mod)*pow(3,k,mod)*\
                   (a+i)*(b+j)*(c+k)%mod
            ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    q = s.count("?")
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    mod = 10**9+7
    ans = 0
    for i in range(q+1):
        for j in range(q+1-i):
            k = q-i-j
            tmp = 1
            tmp *= pow(3,i,mod)
            tmp *= pow(3,j,mod)
            tmp *= pow(3,k,mod)
            tmp *= pow(2,a,mod)
            tmp *= pow(2,b,mod)
            tmp *= pow(2,c,mod)
            tmp %= mod
            ans += tmp
            ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    Q = S.count("?")
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    ans = 0
    for i in range(Q+1):
        for j in range(Q+1-i):
            k = Q - i - j
            ans += (pow(3, i, 10**9+7) * pow(3, j, 10**9+7) * pow(3, k, 10**9+7) * (A+i) * (B+j) * (C+k))
    print(ans % (10**9+7))

=======
Suggestion 7

def main():
    s = input()
    q = 0
    for i in range(len(s)):
        if s[i] == "?":
            q += 1
    print (q)
    ans = 0
    for i in range(q+1):
        ans += 3**i
    print (ans)
    print (ans % (10**9 + 7))

=======
Suggestion 8

def problems104_d():
    pass

=======
Suggestion 9

def solve(S):
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    # 请在这里编写代码
    # 请不要使用已经存在的库函数
    ans = 0
    mod = 10**9 + 7
    for i in range(len(S)):
        if S[i] == 'A':
            ans += (S[i+1:].count('B') * S[i+1

=======
Suggestion 10

def solve():
    s = input()
    n = len(s)
    mod = 10**9+7
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    for i in range(n):
        if s[i] == "A":
            a[i+1] += 1
        elif s[i] == "B":
            b[i+1] += 1
        elif s[i] == "C":
            c[i+1] += 1
        else:
            a[i+1] += 1
            b[i+1] += 1
            c[i+1] += 1
    for i in range(n):
        a[i+1] += a[i]
        b[i+1] += b[i]
        c[i+1] += c[i]
    ans = 0
    for i in range(n):
        if s[i] == "B" or s[i] == "?":
            ans += a[i] * (c[n]-c[i+1])
            ans %= mod
    print(ans)

solve()
