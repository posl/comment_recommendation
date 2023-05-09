Synthesizing 5/10 solutions

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    n = a + b
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(b + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1]
            elif j == b:
                dp[i + 1][j] = dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
    res = ""
    while a > 0 and b > 0:
        if k > dp[a + b - 1][b - 1]:
            res += "b"
            k -= dp[a + b - 1][b - 1]
            b -= 1
        else:
            res += "a"
            a -= 1
    res += "a" * a + "b" * b
    print(res)
    return

=======
Suggestion 2

def ncr(n,r):
    if n<r:
        return 0
    if r==0:
        return 1
    if r==1:
        return n
    if r>n//2:
        return ncr(n,n-r)
    return ncr(n-1,r-1)+ncr(n-1,r)

a,b,k=map(int,input().split())
ans=""
for i in range(a+b):
    if a==0:
        ans+="b"
        b-=1
        continue
    if b==0:
        ans+="a"
        a-=1
        continue
    if k<=ncr(a+b-1,b):
        ans+="a"
        a-=1
    else:
        ans+="b"
        k-=ncr(a+b-1,b)
        b-=1
print(ans)

=======
Suggestion 3

def nCr(n,r):
    import math
    f = math.factorial
    return f(n) / f(r) / f(n-r)

A,B,K = map(int,input().split())
ans = ''
while A>0 and B>0:
    if K > nCr(A+B-1,A-1):
        ans += 'b'
        B -= 1
        K -= nCr(A+B,A)
    else:
        ans += 'a'
        A -= 1
print(ans+'a'*A+'b'*B)

=======
Suggestion 4

def comb(a, b):
    if b == 0:
        return 1
    if a == b:
        return 1
    if a < b:
        return 0
    return comb(a-1, b-1)*a//b

=======
Suggestion 5

def nCr(n,r):
    if n<r:
        return 0
    else:
        return fact[n]//fact[n-r]//fact[r]
fact=[1]*(61)
for i in range(2,61):
    fact[i]=i*fact[i-1]
A,B,K=map(int,input().split())
ans=""
for i in range(A+B):
    if A==0:
        ans+="b"
    elif B==0:
        ans+="a"
    elif K<=nCr(A+B-1,B):
        ans+="a"
        A-=1
    else:
        ans+="b"
        K-=nCr(A+B-1,B)
        B-=1
print(ans)
