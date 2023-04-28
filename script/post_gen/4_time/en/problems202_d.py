Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
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

def main():
    A, B, K = map(int, input().split())
    dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(A+1):
        for j in range(B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ''
    while A > 0 and B > 0:
        if K <= dp[A-1][B]:
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= dp[A-1][B]
            B -= 1
    ans += 'a' * A
    ans += 'b' * B
    print(ans)

=======
Suggestion 4

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 5

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 6

def comb(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1
    return comb(n-1, r-1) * n // r

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    def comb(n, r):
        if n == r or r == 0:
            return 1
        else:
            return comb(n-1, r) + comb(n-1, r-1)
    def dfs(s, a, b, k):
        if a == 0 or b == 0:
            return s + 'a' * a + 'b' * b
        elif k <= comb(a + b - 1, b):
            return dfs(s + 'a', a - 1, b, k)
        else:
            return dfs(s + 'b', a, b - 1, k - comb(a + b - 1, b))
    print(dfs('', A, B, K))

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())
    n = a + b
    c = 1
    for i in range(n):
        if a > 0:
            a -= 1
            c *= n - i
            c //= a + 1
        if c >= k:
            print('a', end='')
        else:
            print('b', end='')
            k -= c

=======
Suggestion 9

def func():
    A, B, K = map(int, input().split())

    def comb(a, b):
        if b == 0 or a == b:
            return 1
        if b == 1 or b == a - 1:
            return a
        return comb(a - 1, b - 1) + comb(a - 1, b)

    ans = ""
    while A + B > 0:
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        if K <= comb(A + B - 1, B):
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= comb(A + B - 1, B)
            B -= 1
    print(ans)
