Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M):
        for j in range(M + 1):
            B[j] += A[i] * C[i - j]
    print(*B)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(n + m):
        for j in range(m + 1):
            b[j] += c[i] * a[i - j]
    print(*b)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0] * (M + 1)
    for i in range(N + M):
        for j in range(M + 1):
            if 0 <= i - j <= N:
                B[j] += A[i - j] * C[i]

    print(*B)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M+1)]
    for i in range(N+1):
        for j in range(M+1):
            B[j] += C[i+j] * A[i]
    print(*B)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i] - sum([A[j]*B[i-j] for j in range(i)])
        print(B[i], end=' ')
    print()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i] - sum([A[j]*B[i-j] for j in range(i)])

    for i in range(M+1):
        print(B[i], end=' ')
    print()

main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M + 1)]
    for i in range(N + 1):
        for j in range(M + 1):
            B[j] += A[i] * C[i + j]
    print(" ".join(map(str, B)))

=======
Suggestion 9

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i]*c[i+j]
    print(*b)

=======
Suggestion 10

def main():
    #N,M=map(int,input().split())
    #A=list(map(int,input().split()))
    #C=list(map(int,input().split()))
    N,M=1,2
    A=[2,1]
    C=[12,14,8,2]
    B=[0]*M
    for i in range(N+M):
        for j in range(M+1):
            if i-j<N+1 and i-j>=0:
                B[j-1]+=A[i-j]*C[i]
    print(*B)
