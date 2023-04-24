Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(range(1, n + 1))
    for i in range(q):
        x = int(input())
        a[x - 1], a[x] = a[x], a[x - 1]
    print(' '.join(map(str, a)))

main()

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        i = A.index(x)
        A[i], A[i+1] = A[i+1], A[i]

    print(*A)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(Q):
        x = X[i]
        ans[x - 1], ans[x] = ans[x], ans[x - 1]
    print(*ans)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        for j in range(N-1):
            if a[j] == x[i]:
                a[j], a[j+1] = a[j+1], a[j]
    print(' '.join(map(str, a)))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        if x[i] == N:
            a[N-1], a[0] = a[0], a[N-1]
        else:
            a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(" ".join(map(str, a)))

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    ans = [0] * N
    for i in range(1, N + 1):
        ans[i - 1] = i

    for x in X:
        ans[x - 1], ans[x] = ans[x], ans[x - 1]

    print(*ans)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(1, N+1):
        A[i] = i
        B[i] = i
    for _ in range(Q):
        x = int(input())
        A[x], A[x+1] = A[x+1], A[x]
    for i in range(1, N+1):
        print(A[i], end=' ')
    print()

=======
Suggestion 8

def solve():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        idx = a.index(x)
        if idx == N - 1:
            a[idx], a[0] = a[0], a[idx]
        else:
            a[idx], a[idx + 1] = a[idx + 1], a[idx]
    print(*a)

=======
Suggestion 9

def main():
    N,Q = map(int, input().split())
    A = [i for i in range(1,N+1)]
    for i in range(Q):
        x = int(input())
        A[x-1],A[x] = A[x],A[x-1]
    print(" ".join(map(str,A)))
main()

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    # print(N, Q)
    # print(X)

    # N = 10
    # Q = 6
    # X = [1, 5, 2, 9, 6, 6]
    # print(N, Q)
    # print(X)

    # N = 7
    # Q = 7
    # X = [7, 7, 7, 7, 7, 7, 7]
    # print(N, Q)
    # print(X)

    # N = 5
    # Q = 5
    # X = [1, 2, 3, 4, 5]
    # print(N, Q)
    # print(X)

    A = list(range(1, N + 1))
    # print(A)

    for x in X:
        index = A.index(x)
        # print("index:", index)
        if index == N - 1:
            A[index], A[0] = A[0], A[index]
        else:
            A[index], A[index + 1] = A[index + 1], A[index]
        # print(A)

    print(*A)
