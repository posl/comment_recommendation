Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems283_b():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        elif query[0] == 2:
            print(a[query[1] - 1])

main()

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        elif query[0] == 2:
            print(A[query[1]-1])

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())

    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            A[int(query[1])-1] = int(query[2])
        else:
            print(A[int(query[1])-1])

=======
Suggestion 5

def problem283_b():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            A[int(query[1])-1] = int(query[2])
        else:
            print(A[int(query[1])-1])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        elif query[0] == 2:
            print(A[query[1] - 1])

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        elif query[0] == 2:
            print(a[query[1] - 1])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        elif query[0] == 2:
            print(a[query[1] - 1])
