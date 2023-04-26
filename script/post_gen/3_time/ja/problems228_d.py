Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

=======
Suggestion 2

def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            while a[x % n] != -1:
                x += 1
            a[x % n] = x
        else:
            print(a[x % n])

=======
Suggestion 3

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
Suggestion 4

def main():
    n = 1048576
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])
    return

=======
Suggestion 5

def main():
    n = 1048576
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h%n] != -1:
                h += 1
            a[h%n] = x
        else:
            print(a[x%n])

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
    q = int(input())
    a = [-1]*1048576
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while a[h%1048576] != -1:
                h += 1
            a[h%1048576] = x
        else:
            print(a[x%1048576])

=======
Suggestion 8

def main():
    q = int(input())
    a = [-1] * (2 ** 20)

    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % (2 ** 20)] != -1:
                h += 1
            a[h % (2 ** 20)] = x
        else:
            print(a[x % (2 ** 20)])

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.readline

    N = 1 << 20
    A = [-1] * N
    Q = int(readline())
    for _ in range(Q):
        t,x = map(int,readline().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 10

def main():
    # input
    Q = int(input())
    TXs = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    A = [-1] * (2**20)
    for T, X in TXs:
        if T == 1:
            h = X
            while A[h%2**20] != -1:
                h += 1
            A[h%2**20] = X
        elif T == 2:
            print(A[X%2**20])

    # output
