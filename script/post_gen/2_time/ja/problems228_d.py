Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = 2 ** 20
    Q = int(input())
    A = [-1] * N
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
    Q = int(input())
    A = [-1] * 1048576
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 1048576] != -1:
                h += 1
            A[h % 1048576] = x
        else:
            print(A[x % 1048576])

=======
Suggestion 3

def main():
    Q = int(input())
    A = [-1] * 1048576
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 1048576] != -1:
                h += 1
            A[h % 1048576] = x
        else:
            print(A[x % 1048576])

=======
Suggestion 4

def main():
    Q = int(input())
    A = [-1] * (2 ** 20)
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % (2 ** 20)] != -1:
                h += 1
            A[h % (2 ** 20)] = x
        else:
            print(A[x % (2 ** 20)])

=======
Suggestion 5

def main():
    Q = int(input())
    A = [-1] * 2 ** 20
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % (2 ** 20)] != -1:
                h += 1
            A[h % (2 ** 20)] = x
        else:
            print(A[x % (2 ** 20)])

=======
Suggestion 6

def main():
    Q = int(input())
    A = [-1] * 2 ** 20
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 2 ** 20] != -1:
                h += 1
            A[h % 2 ** 20] = x
        if t == 2:
            print(A[x % 2 ** 20])

=======
Suggestion 7

def main():
    Q = int(input())
    A = [-1 for i in range(2**20)]
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % (2**20)] != -1:
                h += 1
            A[h % (2**20)] = x
        else:
            print(A[x % (2**20)])

=======
Suggestion 8

def main():
    Q = int(input())
    # A = [-1] * (2 ** 20)
    A = [-1] * 100
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % (2 ** 20)] != -1:
                h += 1
            A[h % (2 ** 20)] = x
        else:
            print(A[x % (2 ** 20)])
