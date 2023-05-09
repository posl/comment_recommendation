Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += A[i] * A[j]
    print(ans % (10**9+7))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            ans += a[i]*a[j]
            ans %= 10**9+7
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n-1):
        for j in range(i+1, n):
            total += a[i]*a[j]
    print(total % (10**9+7))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(N):
        ans += A[i] * sum(A[i+1:])
    print(ans % mod)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    S = sum(A)
    ans = 0
    for a in A:
        S -= a
        ans += a*S
        ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A_list = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A_list[i] * sum(A_list[i+1:])
    print(ans % (10**9+7))

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += A[i] * sum(A[i+1:])
    ans %= (10**9 + 7)

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    mod = 1000000007
    for i in range(n):
        ans += a[i] * (sum(a[i+1:]) % mod)
    print(ans % mod)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    #print(n)
    #print(a)

    sum = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum += a[i] * a[j]
            sum %= (10**9+7)

    print(sum)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7

    sum_a = sum(a)
    sum_a_square = sum([a_i**2 for a_i in a])

    ans = 0

    for a_i in a:
        sum_a -= a_i
        sum_a_square -= a_i**2
        ans += a_i * sum_a
        ans += a_i**2 * (n-1)
        ans -= 2 * a_i * sum_a
        ans %= mod

    print(ans)
