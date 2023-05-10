Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= 10**9+7
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total += A[i] * A[j]
    print(total % (10**9+7))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(N - 1):
        sum -= A[i]
        ans += sum * A[i]
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    s = sum(a)
    for i in range(n):
        s -= a[i]
        ans += a[i]*s
        ans %= MOD
    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 1000000007
    ans = 0
    sum_a = sum(a)
    for i in range(n):
        sum_a -= a[i]
        ans += a[i] * sum_a
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    total = 0
    for i in range(n-1):
        for j in range(i+1, n):
            total += a[i] * a[j]
            total %= mod
    print(total)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    sumA = sum(A)
    for i in range(N):
        sumA -= A[i]
        ans += A[i] * sumA
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum_A = sum(A)
    for i in range(N):
        sum_A -= A[i]
        ans += A[i] * sum_A
    print(ans % (10**9 + 7))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i+1:])
    print(ans % mod)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A[i] * A[j]
    print(ans % (10**9+7))
