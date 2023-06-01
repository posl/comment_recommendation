Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 4
    A = [141421356, 17320508, 22360679, 244949]
    # A = [1,2,3]
    mod = 10**9 + 7
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += A[i] * A[j]
            ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i + 1:])
    print(ans % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    sum = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            sum += A[i] * A[j]
            sum %= mod
    print(sum)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += A[i] * sum(A[i+1:])
    print(ans % (10**9 + 7))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    s = sum(a) % mod
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= mod
    print(ans)

=======
Suggestion 6

def sum_of_products(a):
    a.sort()
    n = len(a)
    s = 0
    for i in range(n):
        s += a[i] * (n - i - 1) * (i + 1)
    return s

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    sum = 0
    for i in range(n):
        sum += a[i] * (sum(a) - a[i])
    print(sum % mod)
main()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_a_square = sum([i**2 for i in a])
    ans = (sum_a**2 - sum_a_square) // 2 % (10**9 + 7)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    sum_a = sum(a)
    for i in range(n-1):
        sum_a -= a[i]
        ans += a[i]*sum_a
        ans %= mod
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 10**9+7
    ans = 0
    for i in range(N):
        ans += A[i]*(sum(A[i+1:])%MOD)
    print(ans%MOD)
