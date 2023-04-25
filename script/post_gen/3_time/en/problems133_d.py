Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = (a[0] + a[1] - a[n-1]) // 2
    for i in range(1, n):
        b[i] = a[i-1] - b[i-1]
    print(*b)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - A[i - 1]
    C = [0] * N
    for i in range(N):
        C[i] = B[i] + B[(i + 1) % N]
    D = [0] * N
    for i in range(N):
        D[i] = C[i] // 2
    print(*D)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = sum(a) - (n - 2) * a[1]
    b[0] //= 2
    for i in range(1, n):
        b[i] = a[i - 1] - b[i - 1]
    print(*b)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A) // (N - 1)
    for i in range(1, N):
        ans[i] = A[i - 1] - ans[0]
    print(" ".join(map(str, ans)))

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N

    for i in range(N):
        ans[i] = A[i] - A[i-1]

    for i in range(N):
        if i % 2 == 0:
            ans[i] = -ans[i]

    for i in range(N):
        ans[i] += ans[i-1]

    for i in range(N):
        ans[i] //= 2

    print(*ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = sum(A)
    X = [0] * N
    X[0] = (S - N * A[0]) // 2
    for i in range(1, N):
        X[i] = A[i - 1] - X[i - 1]

    print(*X)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    B = [0]*N
    for i in range(N):
        B[i] = A[i]
        if i == 0:
            B[i] = A[i] - A[N-1]
        else:
            B[i] = A[i] - A[i-1]
    #print(B)
    C = [0]*N
    for i in range(N):
        C[i] = B[i]*2
    #print(C)
    D = [0]*N
    for i in range(N):
        D[i] = C[i] + C[i-1]
    #print(D)
    E = [0]*N
    for i in range(N):
        E[i] = int(D[i]/2)
    print(*E)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    tmp = 0
    for i in range(N):
        tmp += (A[i] - A[(i+1)%N])
    print(2*tmp, end="")
    for i in range(1, N):
        print(" " + str(2*A[i-1] - tmp), end="")
        tmp = 2*A[i-1] - tmp
    print("")

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # x = (A[0] + A[1] - A[N - 1]) // 2
    # print(x)
    x = (A[0] + A[1] - A[N - 1]) // 2
    ans = [x]
    for i in range(1, N):
        x = A[i - 1] - x
        ans.append(x)
    print(" ".join(map(str, ans)))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    #print(N)
    S = [0] * N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = (A[i-1] - S[i-1]) // 2 + S[i-1]
    #print(S)
    T = [0] * N
    T[0] = S[0]
    for i in range(1, N):
        T[i] = (A[i-1] - T[i-1]) // 2 + S[i]
    #print(T)
    for i in range(N):
        print(T[i] * 2, end = " ")
    print()

main()
