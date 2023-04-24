Synthesizing 10/10 solutions

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

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M + 1):
        for j in range(min(i, N + 1)):
            B[i - j] += A[N - j] * C[i]
    print(*B)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0] * (M+1)
    for i in range(M+1):
        B[i] = C[N+M-i] // A[N]
        for j in range(N+1):
            C[j+M-i] -= B[i] * A[j]

    print(*B)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0] * (M+1)

    for i in range(M+1):
        B[i] = C[i] - sum([A[j] * B[i-j] for j in range(i)])

    print(*B)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    b[0] = c[0]//a[0]
    for i in range(1,m+1):
        b[i] = (c[i] - sum([b[j]*a[i-j] for j in range(i)]))//a[0]
    print(*b)

=======
Suggestion 6

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    return n, m, a, c

=======
Suggestion 7

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    C=list(map(int,input().split()))
    B=[0]*(M+1)
    for i in range(M+1):
        B[i]=C[N+M-i]
        for j in range(N):
            B[i]-=A[N-j]*B[i-j-1]
    print(*B)

=======
Suggestion 8

def solve(n, m, a, c):
    b = [0] * (m + 1)
    b[0] = c[0] // a[0]
    for i in range(1, m + 1):
        b[i] = (c[i] - sum([b[j] * a[i - j] for j in range(i)])) // a[0]
    return b

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))

    B = []
    for i in range(M+1):
        B.append(0)

    for i in range(M+1):
        B[i] = C[i]

    for i in range(M+1):
        for j in range(N+1):
            B[i] -= A[j] * B[i-j]

    for i in range(M+1):
        print(B[i], end=" ")

=======
Suggestion 10

def solve():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)

    B[0] = C[0] // A[0]

    for i in range(1, M+1):
        B[i] = (C[i] - sum([B[j]*A[i-j] for j in range(i)])) // A[0]

    print(*B)
