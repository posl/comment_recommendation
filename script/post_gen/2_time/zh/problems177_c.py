Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += a[i] * a[j]
    print(sum % (10**9 + 7))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += A[i]*A[j]
            sum %= MOD
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    s = sum(a)**2
    t = sum([i**2 for i in a])
    print((s-t)//2%mod)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += A[i]*A[j]
    print(sum % (10**9 + 7))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7

    sum = 0

    for i in range(n):
        sum += a[i] * (sum(a[i+1:]) % mod)

    print(sum % mod)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= mod
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += A[i] * S
        ans %= MOD
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    sum = 0
    for i in range(N-1):
        sum += A[i] * sum(A[i+1:])
    print(sum%(10**9+7))

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum += A[i]*A[j]
    print(sum%(10**9+7))

=======
Suggestion 10

def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += a[i] * a[j]
    print(sum % (10**9+7))
