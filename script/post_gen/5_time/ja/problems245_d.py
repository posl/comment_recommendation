Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0] * (M+1)
    for i in range(N+1):
        for j in range(M+1):
            B[j] += A[i] * C[i+j]
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

    output = ""
    for i in range(M):
        output += str(B[i]) + " "
    output += str(B[M])
    print(output)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0 for i in range(m + 1)]
    for i in range(m + 1):
        b[i] = c[i] - sum([a[j] * b[i - j] for j in range(i)])
    print(*b)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    B[0] = C[0] // A[0]
    for i in range(1, M + 1):
        B[i] = (C[i] - sum([A[j] * B[i - j] for j in range(1, i + 1)])) // A[0]
    print(*B)

=======
Suggestion 5

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0]*(M+1)

    for i in range(M+1):
        for j in range(N+1):
            if i+j <= M:
                B[i] += A[j]*C[i+j]

    print(*B)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = []
    for i in range(m):
        b.append(0)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i] * c[i+j]
    for i in range(m):
        print(b[i], end=" ")
    print(b[m])

=======
Suggestion 7

def get_input():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    return n,m,a,c

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)
    B[0] = C[0] // A[0]
    for i in range(1, M+1):
        B[i] = (C[i] - sum([A[j] * B[i-j] for j in range(1, min(N, i)+1)])) // A[0]
    print(*B)

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b = [0 for i in range(m+1)]
    b[0] = c[0] // a[0]
    for i in range(n+m):
        for j in range(1, min(i+1, m)+1):
            b[j] += c[i+1] * b[j-1]
    print(" ".join(map(str, b)))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[N]
    print(*B)
main()
