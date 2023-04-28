Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    for _ in range(q):
        x = int(input()) - 1
        a[x], a[x+1] = a[x+1], a[x]
    print(*a)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    for _ in range(Q):
        x = int(input()) - 1
        A[x], A[x + 1] = A[x + 1], A[x]
    print(*A)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        A[x-1], A[x] = A[x], A[x-1]

    print(*A)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    A = [i for i in range(1, N+1)]
    for i in range(Q-1, -1, -1):
        A[i], A[i+1] = A[i+1], A[i]
        if A[i+1] == X[i]:
            A[i+1], A[i+2] = A[i+2], A[i+1]
    print(*A)

=======
Suggestion 5

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

=======
Suggestion 6

def swap(i, a):
    tmp = a[i]
    a[i] = a[i+1]
    a[i+1] = tmp
    return a

=======
Suggestion 7

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    xs = [int(input()) for _ in range(Q)]

    # 1 2 3 4 5
    # 1 2 4 3 5
    # 1 2 4 5 3
    # 1 2 5 4 3

    # 1 2 3 4 5 6
    # 1 2 3 4 6 5
    # 1 2 3 6 4 5
    # 1 2 6 3 4 5
    # 1 6 2 3 4 5
    # 6 1 2 3 4 5

    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 7 6
    # 1 2 3 4 7 5 6
    # 1 2 3 7 4 5 6
    # 1 2 7 3 4 5 6
    # 1 7 2 3 4 5 6
    # 7 1 2 3 4 5 6

    # 1 2 3 4 5 6 7 8
    # 1 2 3 4 5 6 8 7
    # 1 2 3 4 5 8 6 7
    # 1 2 3 4 8 5 6 7
    # 1 2 3 8 4 5 6 7
    # 1 2 8 3 4 5 6 7
    # 1 8 2 3 4 5 6 7
    # 8 1 2 3 4 5 6 7

    # 1 2 3 4 5 6 7 8 9
    # 1 2 3 4 5 6 7 9 8
    # 1 2 3 4 5 6 9 7

=======
Suggestion 9

def swap(x, y):
    tmp = x
    x = y
    y = tmp
    return x, y

=======
Suggestion 10

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
