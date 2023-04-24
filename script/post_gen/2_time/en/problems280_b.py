Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i - 1]
    print(*a)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0]*N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(' '.join(map(str, A)))

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    for i in range(N):
        A[i] = S[i] - sum(A[:i])
    print(*A)

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = []
    for i in range(N):
        if i == 0:
            A.append(S[i])
        else:
            A.append(S[i] - sum(A))
    print(" ".join(map(str, A)))

=======
Suggestion 5

def main():
    N = int(input())
    S = [int(x) for x in input().split()]

    A = [0] * N
    for i in range(N):
        if i % 2 == 0:
            A[i] = S[i]
        else:
            A[i] = -S[i]

    for i in range(1, N):
        A[i] += A[i - 1]

    print(' '.join(map(str, A)))

=======
Suggestion 6

def main():
    #N = int(input())
    #S = [int(i) for i in input().split()]
    N = 10
    S = [314159265, 358979323, 846264338, -327950288, 419716939, -937510582, 97494459, 230781640, 628620899, -862803482]
    A = [0]*N
    for i in range(N):
        A[i] = S[i] - sum(A)
    print(A)

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(S[i]-sum(A))
    print(" ".join([str(a) for a in A]))

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))

    # A_1 = S_1
    A = [S[0]]

    # A_i = S_i - S_i-1
    for i in range(1, N):
        A.append(S[i] - S[i-1])

    print(*A)
