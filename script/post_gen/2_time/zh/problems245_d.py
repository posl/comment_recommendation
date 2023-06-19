Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    B[0] = C[0]//A[0]
    for i in range(1, M+1):
        B[i] = (C[i] - sum([B[j]*A[i-j] for j in range(i)]))//A[0]
    print(' '.join(map(str, B)))

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def getB():
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    N = len(A) - 1
    M = len(C) - 1
    B = [0 for _ in range(M+1)]
    for i in range(M, N-1, -1):
        B[i-N] = C[i] // A[N]
        for j in range(N, -1, -1):
            C[i-N+j] -= A[j] * B[i-N]
    for i in range(M, N-1, -1):
        if C[i] != 0:
            return False
    return B

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)
    B[0] = C[0] // A[0]
    for i in range(1, M+1):
        B[i] = (C[i] - sum([A[j] * B[i-j] for j in range(i)])) // A[0]
    print(' '.join(map(str, B)))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[N]
    print(*B)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def getB(A,C):
    N = len(A) - 1
    M = len(C) - 1
    B = [0]*(M+1)
    for i in range(N+1):
        for j in range(M+1):
            B[j] += A[i]*C[j-i]
    return B

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0 for i in range(m+1)]
    b[0] = c[0]//a[0]
    for i in range(1,m+1):
        b[i] = c[i] - sum([b[j]*a[i-j] for j in range(i)])
    print(' '.join(map(str,b)))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + 1):
        B[0] += A[i] * C[i]
    for i in range(1, M + 1):
        B[i] = (C[N + i] - B[0]) // C[i]
    print(' '.join(map(str, B)))

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += c[i]*a[n-i]
    print(" ".join(map(str,b)))
