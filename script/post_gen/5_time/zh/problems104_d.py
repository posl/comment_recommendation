Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = S.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(len(S)):
        if S[i]=='B' or S[i]=='?':
            ans += pow(3,Q,mod)*(S[:i].count('A')+S[i+1:].count('C'))
            ans %= mod
    print(ans)

main()

=======
Suggestion 2

def solve():
    # 解题思路
    # 1. 遍历字符串，统计A、B、C的位置
    # 2. 从左到右遍历字符串，遇到?则加上之前的值，然后加上A、B、C的位置
    # 3. 从右到左遍历字符串，遇到?则加上之后的值，然后加上A、B、C的位置
    # 4. 从左到右遍历字符串，遇到?则加上之前的值，然后加上A、B、C的位置
    # 5. 从右到左遍历字符串，遇到?则加上之后的值，然后加上A、B、C的位置
    # 6. 从左到右遍历字符串，遇到?则加上之前的值，然后加上A、B、C的位置
    # 7. 从右到左遍历字符串，遇到?则加上之后的值，然后加上A、B、C的位置
    # 8. 从左到右遍历字符串，遇到?则加上之前的值，然后加上A、B、C的位置
    # 9. 从右到左遍历字符串，遇到?则加上之后的值，然后加上A、B、C的位置
    # 10. 从左到右遍历字符串，遇到?则加上之前的值，然后加上A、B、C的位置
    # 11. 从右到左遍历字符串，遇到?则加上之后的值，然后加上A、B、C的位置
    # 12. 从左到右遍历字符串，遇到?则加上之前的值，然后加上A、B、C的位置
    # 13. 从右到左遍历字符串，遇到?则加上之后的值，然后加上A、B、C的位置
    #

=======
Suggestion 3

def solve():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    Q = S.count('?')
    S = S.replace('?','')
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == 'B':
            ans += pow(3,Q,mod) * pow(3,i,mod)
        elif S[i] == 'C':
            ans += pow(3,Q,mod) * pow(3,i,mod) * 2
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    q = s.count('?')
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            a = 0
            c = 0
            for j in range(i, n):
                if s[j] == 'A':
                    a += 1
                elif s[j] == 'C':
                    c += 1
                elif s[j] == '?':
                    ans += pow(3, q - 1, mod) * (pow(3, a, mod) + pow(3, c, mod)) % mod
                    ans %= mod
                    q -= 1
                    a += 1
                    c += 1
    print(ans)

main()

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7

    ans = 0
    x = 1
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            ans += x
        x *= 3
        x %= mod

    x = 1
    for i in range(n-1, -1, -1):
        if s[i] == 'B' or s[i] == '?':
            ans += x * pow(3, s[i+1:].count('?'), mod)
        x *= 3
        x %= mod

    print(ans % mod)

=======
Suggestion 7

def main():
    s=input()
    n=len(s)
    mod=10**9+7
    a=[0]*(n+1)
    b=[0]*(n+1)
    c=[0]*(n+1)
    q=0
    for i in range(n):
        if s[i]=="A":
            a[i+1]=a[i]+pow(3,q,mod)
        elif s[i]=="B":
            b[i+1]=b[i]+pow(3,q,mod)
        elif s[i]=="C":
            c[i+1]=c[i]+pow(3,q,mod)
        else:
            a[i+1]=a[i]*3+pow(3,q,mod)
            b[i+1]=b[i]*3+a[i]
            c[i+1]=c[i]*3+b[i]
            q+=1
    print(c[n]%mod)

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
            abc = 3*abc+ab
            ab = 3*ab+a
            a = 3*a+1
        a %= mod
        ab %= mod
        abc %= mod
    print(abc)

=======
Suggestion 9

def main():
    s = input()
    q = s.count("?")
    a = [0] * (q + 1)
    b = [0] * (q + 1)
    c = [0] * (q + 1)
    a[0] = 1
    b[0] = 1
    c[0] = 1
    for i in range(len(s)):
        if s[i] == "A":
            a[1] += a[0]
        elif s[i] == "B":
            b[1] += b[0]
        elif s[i] == "C":
            c[1] += c[0]
        else:
            a[1] += a[0]
            b[1] += b[0]
            c[1] += c[0]
        a[0] = a[1]
        b[0] = b[1]
        c[0] = c[1]
        a[1] %= 1000000007
        b[1] %= 1000000007
        c[1] %= 1000000007
    print(c[0])

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    dp = [[0]*8 for _ in range(n+1)]
    dp[n][0] = 1
    for i in range(n-1,-1,-1):
        for j in range(8):
            if s[i] == "?":
                for k in range(3):
                    dp[i][j] += dp[i+1][j*3+k]
            else:
                dp[i][j] += dp[i+1][j*3+ord(s[i])-ord("A")]
            dp[i][j] %= mod
    print(dp[0][0])
main()
