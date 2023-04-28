Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1]-1] = query[i][2]
        else:
            print(A[query[i][1]-1])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    for q in query:
        if q[0] == 1:
            A[q[1] - 1] = q[2]
        else:
            print(A[q[1] - 1])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split())) # スペース区切り連続数字
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])
