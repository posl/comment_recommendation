Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += a[i]*a[j]
    print(ans % (10**9+7))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += A[i] * A[j]
            ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(N):
        sum -= A[i]
        ans += A[i] * sum
    print(ans % (10**9 + 7))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i+1:])
    print(ans % (10**9+7))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    sum = 0
    for i in range(N):
        sum += A[i]
    ans = 0
    for i in range(N):
        sum -= A[i]
        ans += A[i] * sum % mod
    print(ans % mod)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7

    ans = 0
    for i in range(N-1):
        ans += A[i] * sum(A[i+1:])
        ans %= MOD

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    mod = 10 ** 9 + 7

    ans = 0
    s = 0
    for i in range(N):
        s += A[i]
    for i in range(N):
        s -= A[i]
        ans += (A[i] * s)
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    mod = 10**9 + 7

    ans = 0
    sumA = sum(A)
    for a in A:
        sumA -= a
        ans += a * sumA

    print(ans % mod)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7

    S = 0
    for i in range(N):
        S += A[i]
        S %= MOD

    ans = 0
    for i in range(N):
        S -= A[i]
        S %= MOD
        ans += A[i]*S
        ans %= MOD

    print(ans)

=======
Suggestion 10

def get_ints(): return map(int, sys.stdin.readline().strip().split())
