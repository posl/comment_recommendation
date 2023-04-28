Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M):
        for j in range(min(N, i + 1)):
            B[i - j] -= A[j] * C[i]
    print(*B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    B[0] = C[0] // A[0]
    for i in range(1, M + 1):
        B[i] = (C[i] - sum([B[j] * A[i - j] for j in range(i)])) // A[0]
    print(*B)
main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + 1):
        for j in range(M + 1):
            B[j] += C[i + j] * A[i]
    print(' '.join(map(str, B)))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0 for i in range(M+1)]
    B[0] = C[0] // A[0]
    for i in range(1, M+1):
        B[i] = (C[i] - sum([B[j] * A[i-j] for j in range(i)])) // A[0]

    print(*B)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0 for i in range(m + 1)]
    for i in range(m, -1, -1):
        b[i] = c[i + n]
        for j in range(1, n + 1):
            b[i] -= a[j] * b[i + j]
        b[i] //= a[0]
    print(' '.join(map(str, b)))

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0] * (M+1)
    for i in range(M+1):
        B[i] = C[N+M-i]
        for j in range(N+M-i):
            C[j] -= A[j] * B[i]

    print(*B)

=======
Suggestion 7

def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, M, A, C

=======
Suggestion 8

def calc(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0] * m
for i in range(m):
    b[i] = (c[n + i] - calc(a, b)[n + i]) // a[n]
print(*b)

=======
Suggestion 9

def solve(n, m, a, c):
    b = [0 for _ in range(m + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            b[j] += a[i] * c[i + j]
    return b

=======
Suggestion 10

def solve(n, m, a, c):
    b = [None] * (m + 1)
    b[m] = c[n + m] // a[n]
    for i in range(m - 1, -1, -1):
        b[i] = (c[n + i] - a[n] * b[m]) // a[i]
    return b

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = solve(n, m, a, c)
print(*b)
