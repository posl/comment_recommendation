Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    m = 10**9 + 7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= m
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    C = list(map(int, input().split()))

    C.sort()
    ans = 1
    for i in range(N):
        ans = ans * (C[i] - i) % 1000000007

    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= 1000000007
    print(ans)

solve()

=======
Suggestion 6

def solve():
    N = int(input())
    C = list(map(int, input().split()))

    C.sort()
    MOD = 10**9+7
    ans = 1
    for i in range(N):
        ans = ans * max(C[i]-i, 0) % MOD

    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9 + 7

    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(0, C[i] - i)
        ans %= MOD

    print(ans)

solve()

=======
Suggestion 8

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= (c[i]-i)
        ans %= (10**9+7)
    print(ans)

=======
Suggestion 9

def solve(n, cs):
    # 1. 1<=A[i]<=C[i]
    # 2. A[i]!=A[j]
    # 3. 1<=i<j<=N
    # 1. 1<=A[i]<=C[i] => A[i] = 1,2,3,...,C[i]
    # 2. A[i]!=A[j] => A[i] != A[j] => A[i] = 1,2,3,...,C[i]
    # 3. 1<=i<j<=N => A[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] = 1,2,3,...,C[i]
    # => A[i] = 1,2,3,...,C[i] => C[i] =
