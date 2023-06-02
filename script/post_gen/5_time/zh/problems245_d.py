Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N+1):
        B[0] += C[i] * A[i]
    for j in range(1, M+1):
        B[j] = (C[N+j] - B[0]) // A[0]
    print(*B)
    return 0

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(M+1)
    for i in range(N+M,0,-1):
        B[M-(N+M-i)] = C[i]
        for j in range(0,N+M-i):
            C[j] -= A[j]*C[i]
    print(" ".join(map(str,B)))

=======
Suggestion 3

def solve():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(m+1)
    for i in range(m+1):
        B[m-i] = C[n+m-i]
        for j in range(n+1):
            B[m-i] -= A[n-j]*B[m-i+j]
    print(*B)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    B[0] = C[0] // A[0]
    for i in range(1, M + 1):
        B[i] = (C[i] - sum([B[j] * A[i - j] for j in range(i)])) // A[0]
    print(' '.join(map(str, B)))

solve()

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += c[i]*a[n-i]
    print(*b)

=======
Suggestion 6

def solve():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # 从c中读取出b
    b = [0] * (m + 1)
    for i in range(n + m):
        b[m - i] = c[i] // a[n]

        # 用b更新c
        for j in range(n + 1):
            c[i + j] -= b[m - i] * a[n - j]

    for i in range(m + 1):
        print(b[i], end=' ')
    print()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M, -1, -1):
        B[i] = C[i] // A[N]
        for j in range(N, -1, -1):
            C[i - j] -= B[i] * A[j]
    print(*B)

=======
Suggestion 8

def problem245_d():
    pass

=======
Suggestion 9

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for i in range(M+1)]
    for i in range(M+1):
        for j in range(N+1):
            B[i] += C[i+j] * A[j]
    for i in range(M+1):
        print(B[i], end=" ")
    print()

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    an = list(map(int, input().split()))
    cn = list(map(int, input().split()))
    bn = [0] * (m+1)
    for i in range(n+1):
        for j in range(m+1):
            bn[j] += an[i] * cn[i+j]
    print(' '.join(map(str, bn)))
