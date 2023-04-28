Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= (c[i] - i)
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 1000000007
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    c = list(map(int, input().split()))
    mod = 10**9+7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i]-i, 0)
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int,input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans = (ans*(C[i]-i))%(10**9+7)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    C = list(map(int, input().split()))

    C.sort()

    ans = 1
    for i in range(N):
        ans = ans * (C[i] - i) % 1000000007

    print(ans)

=======
Suggestion 6

def solve(n, c):
    mod = 10**9+7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(0, c[i]-i)
        ans %= mod
    return ans

=======
Suggestion 7

def comb(n, r, mod):
    if r > n:
        return 0
    return fact[n] * factinv[r] * factinv[n-r] % mod

mod = 10**9+7
N = int(input())
C = list(map(int, input().split()))

=======
Suggestion 8

def solve(n, c):
    mod = 10**9 + 7
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * (c[i-1] - i + 1) % mod
    return dp[n]

=======
Suggestion 9

def solve(N, C):
    A = []
    for i in range(N):
        A.append(C[i] - i - 1)
    A.sort()
    #print(A)
    ans = 1
    for i in range(N):
        if A[i] <= 0:
            return 0
        ans = ans * A[i] % (10**9 + 7)
    return ans

=======
Suggestion 10

def read_int():
    return int(input())
