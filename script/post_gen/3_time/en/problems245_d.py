Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M):
        for j in range(min(i + 1, N)):
            B[i - j] += A[N - j] * C[i]
    print(*B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    for i in range(N+1):
        for j in range(M+1):
            B[j] += A[i] * C[i+j]
    print(*B)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0] * (M+1)
    for i in range(M+1):
        B[i] = C[i] - sum([A[j] * B[i-j] for j in range(i)])

    print(*B)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0 for i in range(M+1)]

    for i in range(M+1):
        B[i] = C[i] - sum([A[j]*B[i-j] for j in range(i)])

    print(" ".join(map(str, B)))

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[N+M-i]
        for j in range(N):
            B[i] -= A[j]*B[i+j]
    print(*B)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M + 1)]
    for i in range(M + 1):
        B[i] = C[i] - sum([A[j] * B[i - j] for j in range(i)])
    print(*B)

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b = [0] * (m+1)

    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i] * c[i+j]

    print(*b)

=======
Suggestion 8

def main():
    # Input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # Solve
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i] - sum([a[j] * b[i - j] for j in range(i)])
    print(' '.join(map(str, b)))

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    an = list(map(int, input().split()))
    cm = list(map(int, input().split()))
    bn = [0] * (m+1)

    for i in range(m+1):
        bn[i] = cm[i] - sum([bn[j] * an[i-j] for j in range(i)])

    print(*bn)

=======
Suggestion 10

def main():
    # N, M = map(int, input().split())
    # a = list(map(int, input().split()))
    # c = list(map(int, input().split()))

    N, M = map(int, '1 1'.split())
    a = list(map(int, '100 1'.split()))
    c = list(map(int, '10000 0 -1'.split()))

    b = [0] * (M + 1)
    b[0] = c[0] // a[0]
    for i in range(1, M + 1):
        b[i] = (c[i] - sum([b[j] * a[i - j] for j in range(i)])) // a[0]
    print(' '.join(map(str, b)))
