Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int,

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    b[0] = c[0] // a[n]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i - j] -= a[n - j] * b[i - 1]
        b[i] = c[i] // a[n]
    print(*b)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)

    for i in range(N + M, M, -1):
        for j in range(M, -1, -1):
            B[j] = C[i - j] - sum([A[k] * B[j - k] for k in range(1, j + 1)])
        A = B[:]

    print(*B)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M+1)]
    for i in range(N+M, -1, -1):
        B[M-(N+M-i)] = int((C[i] - sum([A[j]*(i-j) for j in range(N+1)])) / A[N])
    print(*B)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0 for i in range(M+1)]

    for i in range(N+M, N, -1):
        B[M-(N+M-i)] = C[i]
        for j in range(N, -1, -1):
            C[i-(N-j)] -= A[j]*B[M-(N+M-i)]

    for i in range(M, 0, -1):
        B[M-i] = C[i]/A[N]
        for j in range(N, -1, -1):
            C[i-(N-j)] -= A[j]*B[M-i]

    for i in range(M+1):
        print(int(B[i]), end=" ")
    print()

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0 for i in range(m+1)]
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i]*c[i+j]
    print(*b)

=======
Suggestion 7

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    return n, m, a, c

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = []
    for i in range(n+m+1):
        b.append(0)
    for i in range(n+1):
        for j in range(m+1):
            b[i+j] += a[i]*c[j]
    for i in range(m+1):
        print(b[i],end=" ")

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))

    b = [0] * (m+1)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i] * c[i+j]
    print(*b)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #Cの最高次の係数を割る
    a = C[-1]
    A = [a // A[-1] * ai for ai in A]
    C = [ai // A[-1] for ai in C]

    #Aをずらす
    A = [0] * (M + 1) + A

    #Bを計算
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] - sum([B[j] * A[i - j] for j in range(i)])

    print(*B)
