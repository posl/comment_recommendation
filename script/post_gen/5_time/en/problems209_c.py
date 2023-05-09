Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= (c[i] - i)
        ans %= (10**9 + 7)
    print(ans)
    return

=======
Suggestion 3

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * (c[i] - i) % (10**9 + 7)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9+7
    ans = 1
    for i in range(N):
        ans *= max(0, C[i]-i)
        ans %= mod
    print(ans)

=======
Suggestion 5

def problems209_c():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9+7
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(C[i]-i, 0)
        ans %= MOD
    print(ans)

=======
Suggestion 6

def solve(n, c):
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 10**9 + 7
    return ans

n = int(input())
c = list(map(int, input().split()))
print(solve(n, c))

=======
Suggestion 7

def solve(N, C):
    MOD = 10**9 + 7
    C.sort()
    ans = 1
    for i, c in enumerate(C):
        ans = ans * max(0, c - i) % MOD
    return ans

=======
Suggestion 8

def solve(N, C):
    ans = 1
    C.sort()
    for i, c in enumerate(C):
        ans *= max(0, c - i)
        ans %= 10**9 + 7
    return ans

N = int(input())
C = list(map(int, input().split()))
print(solve(N, C))

=======
Suggestion 9

def solve(n, c):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    last = {}
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if c[i - 1] in last and last[c[i - 1]] != i - 1:
            dp[i] += dp[last[c[i - 1]]]
        last[c[i - 1]] = i
        dp[i] %= MOD
    return dp[n]

=======
Suggestion 10

def main():
    # Read from Standard Input
    N = int(input())
    C = list(map(int, input().split()))
    # Solve the problem
    MOD = 10**9+7
    C.sort()
    ans = 1
    for i in range(N):
        ans = ans * max(C[i]-i, 0) % MOD
    # Write the answer to Standard Output
    print(ans)
