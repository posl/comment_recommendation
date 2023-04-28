Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = 1048576
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 2

def main():
    N = 2 ** 20
    A = [-1] * N

    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 3

def main():
    N = 1048576
    A = [-1] * N
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
    return

=======
Suggestion 4

def main():
    N = 2**20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        x %= N
        if t == 1:
            while A[x] != -1:
                x += 1
                x %= N
            A[x] = x
        else:
            print(A[x])
    return

=======
Suggestion 5

def main():
    N = 2**20
    A = [-1 for i in range(N)]
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 6

def main():
    n = 2**20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        x %= n
        if t == 1:
            while a[x] != -1:
                x += 1
                x %= n
            a[x] = x
        else:
            print(a[x])

=======
Suggestion 7

def main():
    n = int(input())
    a = [-1] * (2 ** 20)
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % (2 ** 20)] != -1:
                h += 1
            a[h % (2 ** 20)] = x
        else:
            print(a[x % (2 ** 20)])

=======
Suggestion 8

def main():
    n = int(input())
    a = [-1] * (2 ** 20)
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            while a[x % (2 ** 20)] != -1:
                x += 1
            a[x % (2 ** 20)] = x
        else:
            print(a[x % (2 ** 20)])

=======
Suggestion 9

def main():
    n = 2**20
    q = int(input())
    a = [-1] * n
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

=======
Suggestion 10

def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for i in range(q):
        t, x = map(int, input().split())
        h = x
        if t == 1:
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])
