Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a):
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i + 1:])
        ans %= mod
    return ans

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += a[i] * a[j]
    print(ans % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    sum_A = sum(A)
    sum_A2 = sum([a**2 for a in A])
    ans = (sum_A**2 - sum_A2) // 2 % mod
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum += a[i]*a[j]
    print(sum%mod)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i]*s
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    sum_a = sum(a)
    sum_a2 = sum([i**2 for i in a])
    print(((sum_a**2 - sum_a2) // 2) % mod)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            ans += a[i]*a[j]
    print(ans%(10**9+7))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    sum_A = sum(A)
    ans = 0
    for a in A:
        sum_A -= a
        ans += a * sum_A
        ans %= MOD
    print(ans)

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n - 1):
        sum += a[i] * sum(a[i + 1:])
    print(sum % (10 ** 9 + 7))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += a[i]*a[j]
    print(ans%(10**9+7))
