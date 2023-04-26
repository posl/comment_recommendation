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
        elif query[0] == 2:
            print(A[query[1]-1])

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        else:
            print(a[query[1]-1])

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = [list(map(int,input().split())) for i in range(Q)]

    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1]-1] = query[i][2]
        elif query[i][0] == 2:
            print(A[query[i][1]-1])

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    #クエリ処理
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 6

def main():
    # input
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int,input().split())))
    # output
    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1]-1] = query[i][2]
        else:
            print(A[query[i][1]-1])
    return
