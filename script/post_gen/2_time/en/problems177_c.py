Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        ans += A[i] * sum(A[i+1:])
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += A[i] * S
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * a[i]
        ans %= mod
    ans *= n * (n-1) // 2
    ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - 1)
        ans %= 1000000007
    for i in range(N):
        for j in range(i + 1, N):
            ans -= 2 * A[i] * A[j]
            ans %= 1000000007
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - i - 1)
        ans %= 10**9 + 7
    for i in range(N - 1, 0, -1):
        ans += A[i] * A[i] * i
        ans %= 10**9 + 7
    for i in range(N - 1):
        ans -= A[i] * A[i + 1] * 2
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(N):
        ans += A[i]*A[i]
        ans %= MOD
    for i in range(N):
        for j in range(i+1, N):
            ans += 2*A[i]*A[j]
            ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i] * A[i+1]
    print(sum)

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    Asum = sum(A)
    for i in range(N):
        Asum -= A[i]
        ans += A[i] * Asum
        ans %= MOD
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    mod = 10**9 + 7
    a.sort()
    s = 0
    for i in range(n-1):
        s += (a[i] * (a[i+1] - a[i]) * (n - i - 1)) % mod
        s %= mod
    print(s)
