Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    Q = int(input())
    A = [-1]*(2**20)
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%len(A)] != -1:
                h += 1
            A[h%len(A)] = x
        else:
            print(A[x%len(A)])

=======
Suggestion 3

def main():
    q = int(input())
    a = [-1 for i in range(2**20)]
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % (2**20)] != -1:
                h += 1
            a[h % (2**20)] = x
        else:
            print(a[x % (2**20)])

=======
Suggestion 4

def main():
    Q = int(input())
    A = [-1 for _ in range(2**20)]
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 2**20] != -1:
                h += 1
            A[h % 2**20] = x
        else:
            print(A[x % 2**20])

=======
Suggestion 5

def main():
    N = 2**20
    A = [-1 for _ in range(N)]
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
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = 2**20
    Q = int(input())
    A = [-1]*N
    dq = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
            dq.append(h%N)
        else:
            while A[x%N] == -1:
                x += 1
            print(A[x%N])
            A[x%N] = -1
            while dq and A[dq[0]] == -1:
                dq.popleft()
            if dq:
                A[dq[0]] = x
                dq.append(dq.popleft())

=======
Suggestion 7

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
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline

    N = 2**20
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
Suggestion 9

def solve():
    n = 1048576
    q = int(input())
    a = [-1 for _ in range(n)]
    for _ in range(q):
        t, x = map(int,input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])
