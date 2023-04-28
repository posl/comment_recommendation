Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])

=======
Suggestion 2

def main():
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
Suggestion 3

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

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A[q[1]-1] = q[2]
        elif q[0] == 2:
            print(A[q[1]-1])
        else:
            print("Error")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for q in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        else:
            print(a[query[1]-1])

=======
Suggestion 7

def main():
    n = int(input())
    an = list(map(int, input().split()))
    q = int(input())
    for i in range(0,q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            an[query[1]-1] = query[2]
        else:
            print(an[query[1]-1])

=======
Suggestion 8

def problems283_b():
    return None
