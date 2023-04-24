Synthesizing 10/10 solutions

=======
Suggestion 1

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
        if t == 2:
            print(A[x % 1048576])

=======
Suggestion 2

def main():
    N = 2**20
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
Suggestion 3

def main():
    Q = int(input())
    A = [-1] * (2**20)
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % (2**20)] != -1:
                h += 1
            A[h % (2**20)] = x
        else:
            print(A[x % (2**20)])

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
    N = 2**20
    A = [-1]*N
    Q = int(input())
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        elif t == 2:
            print(A[x%N])

=======
Suggestion 6

def main():
    N = 2**20
    A = [-1]*N
    Q = int(input())
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        else:
            print(A[x%N])

main()

=======
Suggestion 7

def main():
    n = 2**20
    a = [-1]*n
    q = int(input())
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h%n] != -1:
                h += 1
            a[h%n] = x
        else:
            print(a[x%n])
    return

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
    input = sys.stdin.readline
    Q = int(input())
    A = [-1]*1048576
    for _ in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h%1048576] != -1:
                h += 1
            A[h%1048576] = x
        else:
            print(A[x%1048576])

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    N = 2**20
    A = [-1]*N
    Q = int(input())
    q = deque()
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            q.append(x)
        else:
            if A[x%N] == -1:
                A[x%N] = q.popleft()
            print(A[x%N])
    return
