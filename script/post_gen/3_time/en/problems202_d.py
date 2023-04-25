Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nCr(n,r):
    r = min(r,n-r)
    numer = reduce(op.mul,xrange(n,n-r,-1),1)
    denom = reduce(op.mul,xrange(1,r+1),1)
    return numer//denom

=======
Suggestion 2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 3

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 4

def solve():
    A, B, K = map(int, input().split())
    n = A + B
    dp = [[0] * (B + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(B + 1):
            if j < B:
                dp[i + 1][j + 1] += dp[i][j]
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
    ans = ""
    while A + B > 0:
        if A > 0:
            tmp = dp[A + B - 1][B]
            if tmp >= K:
                ans += "a"
                A -= 1
            else:
                ans += "b"
                B -= 1
                K -= tmp
        else:
            ans += "b"
            B -= 1
    print(ans)

=======
Suggestion 5

def get_combination(a, b):
    if a == 0 or b == 0:
        return 1
    else:
        return get_combination(a - 1, b) + get_combination(a, b - 1)

=======
Suggestion 6

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    ans = ''
    for i in range(a):
        ans += 'a'
    for i in range(b):
        ans += 'b'
    print(ans)
    for i in range(k-1):
        ans = next(ans)
        print(ans)
    print(ans)

=======
Suggestion 8

def nCr(n,r):
    f=math.factorial
    return f(n) / f(r) / f(n-r)

import math
A,B,K = map(int, input().split())
ans = []
for i in range(A):
    ans.append('a')
for i in range(B):
    ans.append('b')
for i in range(A+B):
    if A == 0 or B == 0:
        break
    if K <= nCr(A+B-1,A-1):
        ans[A+B-1-i] = 'a'
        A -= 1
    else:
        K -= nCr(A+B-1,A-1)
        ans[A+B-1-i] = 'b'
        B -= 1
print(''.join(ans))

=======
Suggestion 9

def main():
    A, B, K = map(int, input().split())
    print(lexicographic(A, B, K))
