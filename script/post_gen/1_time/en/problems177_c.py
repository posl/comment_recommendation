Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for a in A:
        S -= a
        ans += a * S
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += a[i] * sum(a[i+1:])
    print(ans % (10**9+7))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for a in A:
        S -= a
        ans += a * S
    print(ans % (10**9 + 7))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * a[i] * (n - 1)
        ans %= mod
    for i in range(n):
        ans -= a[i] * a[i]
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - 1)
        ans %= 10 ** 9 + 7
    for i in range(N - 1):
        ans -= A[i] * A[i + 1] * 2
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    MOD = 10**9+7
    ans = 0
    for i in range(N-1):
        ans += A[i] * (A[i+1] - A[i]) * (N - i - 1)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i - N + 1) * 2
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i * (N - 1 - i) + (N - 1 - i) * (N - 1 - i - 1) // 2)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A

    ans = 0
    for i in range(1, N+1):
        ans += A[i] * (i * (N-i+1) + (N-i+1) * (N-i) // 2)

    print(ans % (10**9+7))

=======
Suggestion 10

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]

    # (A_1 + A_2 + ... + A_N) ^ 2 - (A_1^2 + A_2^2 + ... + A_N^2)
    # = 2 * (A_1A_2 + A_1A_3 + ... + A_1A_N + A_2A_3 + ... + A_{N-1}A_N)
    # = 2 * (A_1A_2 + A_1A_3 + ... + A_1A_N + A_2A_3 + ... + A_{N-1}A_N)
    # = 2 * sum_{i=1}^{N-1}sum_{j=i+1}^{N} A_i A_j
    # = 2 * sum_{i=1}^{N}sum_{j=i+1}^{N} A_i A_j
    # = 2 * sum_{i=1}^{N} A_i * sum_{j=i+1}^{N} A_j
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{
