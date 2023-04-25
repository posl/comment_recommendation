Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(0, C[i] - i)
        ans %= 10**9+7
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(0, C[i] - i)
        ans %= 1000000007
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(n):
        ans = ans * max(0, c[i]-i) % mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= (C[i]-i)
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans = ans * max(0, C[i] - i) % 1000000007
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        ans = (ans * (C[i] - i)) % mod
    print(ans)
solve()

=======
Suggestion 7

def main():
    N = int(input())
    C = list(map(int, input().split()))

    C.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        ans = (ans * max(0, C[i]-i)) % mod
    print(ans)

=======
Suggestion 8

def count_seq(N, C):
    mod = 10**9 + 7
    C.sort()
    count = 1
    for i in range(N):
        count *= C[i] - i
        count %= mod
    return count

=======
Suggestion 9

def main():
    N = int(input())
    C = list(map(int, input().split()))
    print()
    print(C)
    print(N)
    print()

=======
Suggestion 10

def solve(n, c):
    mod = 10**9 + 7

    # dp[i]: number of sequences satisfying the conditions
    dp = [1] * n

    # cum[i]: cumulative sum of dp[i]
    cum = [0] * n
    cum[0] = dp[0]
    for i in range(1, n):
        cum[i] = cum[i - 1] + dp[i]

    # last[j]: the last index of j
    last = [-1] * (max(c) + 1)
    for i in range(n):
        last[c[i]] = i

    for i in range(1, n):
        if c[i - 1] == c[i]:
            dp[i] = cum[i - 1]
        elif last[c[i]] < i - 1:
            dp[i] = cum[i - 1]
        else:
            dp[i] = (cum[i - 1] - cum[last[c[i]] - 1]) % mod

    return dp[-1]
