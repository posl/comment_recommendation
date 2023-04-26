Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k,q = map(int,input().split())
    a = [0] * n
    for i in range(q):
        a[int(input())-1] += 1
    for i in range(n):
        if k - q + a[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def solve():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    B = [0] * N
    for i in range(Q):
        B[A[i]-1] += 1
    for i in range(N):
        if K - (Q - B[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    point = [K-Q] * N
    for a in A:
        point[a-1] += 1
    for p in point:
        if p > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q] * N
    for a in A:
        score[a - 1] += 1
    for s in score:
        if s > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [K - Q] * N
    for a in A:
        ans[a - 1] += 1
    for i in range(N):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    A = [0] * Q
    for i in range(Q):
        A[i] = int(input())
    B = [K - Q] * N
    for i in range(Q):
        B[A[i] - 1] += 1
    for i in range(N):
        if B[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n,k,q = map(int,input().split())
    point = [k] * n
    for i in range(q):
        a = int(input())
        point[a-1] += 1
    for j in range(n):
        if point[j] - q <= 0:
            print('No')
        else:
            print('Yes')

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]

    point = [K] * N
    for i in range(Q):
        point[A[i] - 1] += 1

    for i in range(N):
        if point[i] - Q <= 0:
            print("No")
        else:
            print("Yes")

=======
Suggestion 9

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    result = [k-q for _ in range(n)]
    for i in range(q):
        result[a[i]-1] += 1
    for i in range(n):
        if result[i] <= 0:
            print('No')
        else:
            print('Yes')

=======
Suggestion 10

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]

    scores = [k-q for _ in range(n)]

    for i in range(q):
        scores[a[i]-1] += 1

    for i in range(n):
        if scores[i] > 0:
            print("Yes")
        else:
            print("No")
