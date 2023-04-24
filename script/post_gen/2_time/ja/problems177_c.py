Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            sum += A[i] * A[j]
    print(sum % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = sum(a)
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    s = sum(a)
    ans = 0
    for i in a:
        s -= i
        ans += i*s
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i+1:])
        ans %= mod
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * sum(A[i+1:])
    print(ans % (10**9+7))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7

    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i]*s

    print(ans%mod)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    sum = 0
    for i in range(N-1):
        sum += A[i] * sum(A[i+1:N])
    print(sum%mod)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    sumA = sum(A)%mod
    for i in range(N-1):
        sumA -= A[i]
        ans += A[i]*sumA
        ans %= mod
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    mod = 10**9 + 7

    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += a_list[i] * a_list[j]
            sum %= mod

    print(sum)
