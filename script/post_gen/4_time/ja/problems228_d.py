Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = 2**20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        else:
            print(A[x%N])

=======
Suggestion 2

def main():
    N = 2**20
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
Suggestion 3

def main():
    N = 2**20
    A = [-1]*N
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        else:
            print(A[x%N])

=======
Suggestion 4

def main():
    q = int(input())
    a = [-1] * (2 ** 20)
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % (2 ** 20)] != -1:
                h += 1
            a[h % (2 ** 20)] = x
        else:
            print(a[x % (2 ** 20)])

=======
Suggestion 5

def main():
    N = 1048576
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
    Q = int(input())
    A = [-1] * 2**20
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            while A[x % 2**20] != -1:
                x += 1
            A[x % 2**20] = x
        elif t == 2:
            print(A[x % 2**20])

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 1048576
    N = 2 ** 20
    A = [-1] * N
    Q = int(readline())
    for _ in range(Q):
        t, x = map(int, readline().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 8

def main():
    # ここに回答を書く
    N = 2 ** 20
    A = [-1] * N
    Q = int(input())
    for i in range(0, Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
