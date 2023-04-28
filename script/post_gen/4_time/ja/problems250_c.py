Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    for i in range(q):
        x = int(input())
        a[x-1], a[x] = a[x], a[x-1]
    print(*a)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    balls = list(range(1, n+1))
    for i in range(q):
        x = int(input())
        balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)

=======
Suggestion 3

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    A = [i for i in range(1, N+1)]
    for x in X:
        A[x-1], A[x] = A[x], A[x-1]
    print(*A)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    for _ in range(Q):
        x = int(input())
        index = A.index(x)
        A[index], A[index - 1] = A[index - 1], A[index]
    print(*A)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(range(1,N+1))
    for i in range(Q):
        x = int(input())
        a = A.index(x)
        A[a], A[a-1] = A[a-1], A[a]
    print(*A)

=======
Suggestion 7

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

=======
Suggestion 8

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

=======
Suggestion 9

def swap(x):
    tmp = x[0]
    x[0] = x[1]
    x[1] = tmp
    return x

=======
Suggestion 10

def swap(a, b):
    return b, a
