Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k,q = map(int,input().split())
    a = [0]*n
    for i in range(q):
        a[int(input())-1] += 1
    for i in range(n):
        if k - q + a[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    # input
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    # compute

    # output
    for i in range(1, N+1):
        if K - Q + A.count(i) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    n, k, q = map(int, input().split())
    score = [0] * n
    for i in range(q):
        a = int(input())
        score[a-1] += 1

    for i in range(n):
        if k - q + score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K - Q] * N
    for a in A:
        scores[a - 1] += 1
    for score in scores:
        if score > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    score = [0] * N
    for a in A:
        score[a-1] += 1

    for s in score:
        if K - Q + s > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    p = [k - q] * n
    for _ in range(q):
        a = int(input())
        p[a-1] += 1
    for i in range(n):
        if p[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, K, Q = map(int, input().split())
    A = []
    for i in range(Q):
        A.append(int(input()))
    score = [K] * N
    for i in range(Q):
        score[A[i]-1] += 1
    for i in range(N):
        if score[i] > Q:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = []
    for i in range(Q):
        A.append(int(input()))
    S = [K-Q] * N
    for i in range(Q):
        S[A[i]-1] += 1
    for i in range(N):
        if S[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N,K,Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [0] * N

    for i in range(Q):
        scores[A[i]-1] += 1

    for i in range(N):
        if K - (Q - scores[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def solve():
    # Implement here
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K - Q] * N
    for a in A:
        scores[a - 1] += 1
    for score in scores:
        if score <= 0:
            print('No')
        else:
            print('Yes')
