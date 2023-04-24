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
    print(*B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i]
        for j in range(N + 1):
            B[i] -= A[j] * B[i - j]
        B[i] //= A[0]
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

    print(' '.join(map(str, B)))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i]//A[0]
        for j in range(N+1):
            C[i+j] -= A[j]*B[i]
    print(*B)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i]
        for j in range(N):
            B[i] -= A[j]*B[i-j-1]
        B[i] /= A[0]
    print(" ".join(map(str, B)))

=======
Suggestion 6

def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, M, A, C

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [C[i] for i in range(N, N+M+1)]
    for i in range(M):
        B[i] -= sum([A[j]*B[i+j+1] for j in range(N)])
        B[i] //= A[0]
    print(' '.join(map(str, B)))

=======
Suggestion 8

def solve(N,M,A,C):
    B = [0]*(M+1)
    B[M] = C[N+M]//A[N]
    for i in range(M):
        B[M-1-i] = (C[N+M-1-i]-sum(B[M-i:])*A[N-1-i])//A[N]
    return B

=======
Suggestion 9

def get_ints(): return map(int, input().split())
