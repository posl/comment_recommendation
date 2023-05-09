Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] - sum([A[j] * B[i - j] for j in range(i)])
    print(*B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + 1):
        for j in range(M + 1):
            B[j] += A[i] * C[i + j]
    print(*B)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(n + m):
        for j in range(min(i + 1, n)):
            b[i - j] += a[n - j - 1] * c[i]
    print(*b)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b = [0] * (m + 1)
    for i in range(n + m, n, -1):
        b[m] = c[i]
        for j in range(n, -1, -1):
            c[j + m - n] -= a[j] * b[m]
        m -= 1

    print(" ".join(map(str, b)))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0]*(m+1)
    for i in range(m+1):
        b[i] = c[n+m-i]
        for j in range(n+1):
            b[i] -= a[j]*c[n+m-i-j]
    print(*b)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m+1)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i] * c[i+j]
    print(" ".join(map(str, b)))

=======
Suggestion 7

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    for i in range(N+1):
        for j in range(M+1):
            if i+j > N+M:
                break
            B[j] += A[i]*C[i+j]
    print(*B)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b = [0 for i in range(m+1)]
    for i in range(m+1):
        b[i] = c[i] - sum([a[j] * b[i-j] for j in range(i)])

    print(*b)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))

    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i] - sum([A[j]*B[i-j] for j in range(i)])
    print(" ".join(map(str,B)))
