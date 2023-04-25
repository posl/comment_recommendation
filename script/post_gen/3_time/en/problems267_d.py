Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]

    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, B[i + M] - B[i])

    print(ans)

main()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] + (i + 1)
    b.sort(reverse=True)
    print(sum(b[:m]))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] + (i + 1)
    c = [0] * (n - m + 1)
    for i in range(n - m + 1):
        c[i] = b[i] + b[i + m - 1]
    print(max(c))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[:M]))

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A, reverse=True)
    ans = 0
    for i in range(M):
        ans += B[i] * (i + 1)
    print(ans)

solve()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:m]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted([(a[i], i) for i in range(n)], reverse=True)
    ans = 0
    for i in range(m):
        ans += (i + 1) * b[i][0]
    print(ans)

main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(i, N + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + i * A[j])
    print(dp[M][N])

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            b.sort()
            ans = max(ans, sum(b[-m:]))

    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        ans += (i+1) * a
    ans -= sum(A[M:])
    print(ans)
