Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    # print("solve")
    N = 2 ** 20
    # print(N)
    A = [-1] * N
    # print(A)
    Q = int(input())
    # print(Q)
    for i in range(Q):
        # print(i)
        t, x = map(int, input().split())
        # print(t)
        # print(x)
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])


solve()

=======
Suggestion 2

def solve():
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
Suggestion 3

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
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N = 2 ** 20
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

=======
Suggestion 6

def main():
    n = 2 ** 20
    a = [-1 for _ in range(n)]
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
Suggestion 7

def main():
    Q = int(input())
    A = [-1] * (2**20)
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 2**20] != -1:
                h += 1
            A[h % 2**20] = x
        else:
            print(A[x % 2**20])

=======
Suggestion 8

def solve():
    N = 2 ** 20
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

=======
Suggestion 9

def main():
    N = 2 ** 20
    A = [0] * N
    Q = int(input())
    for i in range(Q):
        line = input().split()
        t = int(line[0])
        x = int(line[1])
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
