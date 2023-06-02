Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

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
    print("hello world!")

=======
Suggestion 4

def main():
    A = [-1] * 1048576
    Q = int(input())
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
Suggestion 5

def main():
    n = 2**20
    A = [-1] * n
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % n] != -1:
                h += 1
            A[h % n] = x
        else:
            print(A[x % n])

=======
Suggestion 6

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
