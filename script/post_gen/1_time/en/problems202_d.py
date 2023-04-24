Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 2

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 3

def nCr(n,r):
    if n<r:
        return 0
    else:
        r = min(r,n-r)
        numer = reduce(op.mul,xrange(n,n-r,-1),1)
        denom = reduce(op.mul,xrange(1,r+1),1)
        return numer//denom

import operator as op
A,B,K = map(int,raw_input().split())

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    S = A + B
    ans = ""
    for i in range(S):
        if A == 0:
            ans += "b"
            continue
        if B == 0:
            ans += "a"
            continue
        tmp = 1
        for j in range(1, A + 1):
            tmp *= (S - j + 1)
            tmp //= j
            if K <= tmp:
                ans += "a"
                A -= 1
                break
            else:
                K -= tmp
                ans += "b"
                B -= 1
    print(ans)

=======
Suggestion 5

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

=======
Suggestion 6

def nCr(n,r):
    return int( reduce(lambda x,y:x*y, range(n-r+1, n+1)) / reduce(lambda x,y:x*y, range(1, r+1)) )

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    print(get_string(A, B, K))
