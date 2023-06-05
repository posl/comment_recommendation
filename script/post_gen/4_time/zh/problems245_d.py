Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i]-sum([A[j]*B[i-j] for j in range(i)])
    print(" ".join(map(str,B)))

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = []
    for i in range(m+1):
        b.append(0)
    b[0] = c[0]//a[0]
    for i in range(1,m+1):
        b[i] = (c[i] - sum([b[j]*a[i-j] for j in range(i)]))//a[0]
    print(' '.join(map(str,b)))

=======
Suggestion 3

def get_input():
    # N M
    # A_0 A_1 ...A_{N-1} A_N
    # C_0 C_1 ...C_{N+M-1} C_{N+M}
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, M, A, C

=======
Suggestion 4

def solve(a, c):
    n = len(a) - 1
    m = len(c) - 1
    b = [0] * (m + 1)
    for j in range(m, n, -1):
        b[j - n] = c[j] // a[n]
        for i in range(n + 1):
            c[i + j - n] -= b[j - n] * a[i]
    return b

=======
Suggestion 5

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    C=list(map(int,input().split()))
    B=[0]*(M+1)
    for i in range(N+M,0,-1):
        B[M]=int((C[i]-sum([A[j]*B[j] for j in range(M)]))/A[N])
        for j in range(M):
            B[j]=B[j]+A[j]*B[M]
    print(' '.join(map(str,B)))

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    B[0] = C[0] // A[-1]
    for i in range(M + 1):
        for j in range(N):
            B[i] -= B[i - j - 1] * A[j]
        if i == M:
            break
        B[i + 1] = C[i + 1] // A[-1]
    print(' '.join(map(str, B)))

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))

    B = [0] * (M+1)
    for i in range(N+1):
        B[0] += A[i] * C[i]
    for i in range(1,M+1):
        B[i] = C[N+i] - B[0]
    print(*B)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0 for i in range(M+1)]
    for i in range(M+1):
        B[i] = C[i] - sum(A[j]*B[i-j] for j in range(i))
    print(*B)

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (M + 1)
    b[0] = c[0] // a[0]
    for i in range(1, M + 1):
        b[i] = (c[i] - sum([b[j] * a[i - j] for j in range(i)])) // a[0]
    print(*b[::-1])


solve()
