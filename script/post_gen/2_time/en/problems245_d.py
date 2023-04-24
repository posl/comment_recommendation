Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]
        for j in range(N + 1):
            C[i + j] -= B[i] * A[j]
    print(' '.join(map(str, B)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]
        for j in range(N + 1):
            C[i + j] -= A[j] * B[i]
    print(*B)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]
        for j in range(N + 1):
            C[i + j] -= B[i] * A[j]
    print(*B)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + 1):
        B[0] -= A[i] * C[i]
    for i in range(M):
        B[i + 1] = C[i] - B[0] * A[i + 1]
    print(' '.join(map(str, B)))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i]
        for j in range(n + 1):
            if i >= j:
                b[i] -= a[j] * b[i - j]
    print(*b)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)
    for i in range(M+1):
        B[i] = C[i]
        for j in range(N+1):
            B[i] -= A[j] * B[i-j]
        B[i] /= A[0]
    print(*B)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i]
        for j in range(i):
            B[i] -= A[j]*B[i-j-1]
        B[i] //= A[i]
    print(*B)
