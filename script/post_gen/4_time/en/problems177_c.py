Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += A[i] * A[j]
    print(sum % (10**9+7))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    sum_a = sum(a)
    for i in range(n-1):
        sum_a -= a[i]
        ans += a[i] * sum_a
    print(ans % (10**9+7))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7

    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += A[i]*A[j]
            sum %= mod

    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i+1:])
    print(ans%(10**9+7))

=======
Suggestion 5

def solve():
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

    ans = 0
    total = sum(a)
    for i in range(n):
        total -= a[i]
        ans += a[i] * total

    print(ans % (10**9 + 7))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    mod = 10**9+7
    sum_a = sum(a)
    sum_a2 = sum([i**2 for i in a])
    print((sum_a**2-sum_a2)//2%mod)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    sum_a = sum(A)
    sum_a_square = sum([a**2 for a in A])
    print(((sum_a**2 - sum_a_square)//2)%MOD)

=======
Suggestion 9

def sum_n(n):
    return n*(n+1)//2

N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

sum_A = sum(A)
sum_A2 = sum([a*a for a in A])
ans = 0

for i in range(N):
    sum_A -= A[i]
    sum_A2 -= A[i]*A[i]
    ans += A[i]*sum_A
    ans -= A[i]*A[i]*(N-1)
    ans -= A[i]*sum_n(N-1)
    ans += sum_A2
    ans %= mod

print(ans)
