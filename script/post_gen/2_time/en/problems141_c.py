Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = [0] * N
    for i in range(Q):
        A[int(input()) - 1] += 1
    for i in range(N):
        if K - (Q - A[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K for _ in range(N)]
    for i in range(Q):
        scores[A[i]-1] += 1
    for i in range(N):
        if scores[i] - Q > 0:
            print("Yes")
        else:
            print("No")
    return

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    score = [K - Q] * N
    for i in range(Q):
        score[A[i] - 1] += 1

    for i in range(N):
        if score[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    score = [k - q for _ in range(n)]
    for i in range(q):
        score[a[i] - 1] += 1
    for i in range(n):
        if score[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    B = [K - Q] * N
    for i in range(Q):
        B[A[i] - 1] += 1
    for i in range(N):
        if B[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    b = [k-q] * n
    for i in range(q):
        b[a[i]-1] += 1
    for i in range(n):
        if b[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    for i in range(1, N+1):
        if K - (Q - A.count(i)) > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    point = [k-q for _ in range(n)]
    for i in range(q):
        point[a[i]-1] += 1
    for i in range(n):
        print("Yes" if point[i] > 0 else "No")

=======
Suggestion 9

def main():
    #input
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    #output
    for i in range(N):
        print("Yes" if K-Q+A.count(i+1)>0 else "No")

=======
Suggestion 10

def main():
    # Read data
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    # Solve
    score = [K - Q] * N
    for i in range(Q):
        score[A[i] - 1] += 1

    # Output
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")
