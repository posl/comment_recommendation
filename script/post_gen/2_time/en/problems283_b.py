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
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

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
        else:
            print(a[query[1] - 1])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        else:
            print(a[query[1]-1])

main()

=======
Suggestion 5

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

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            A[int(query[1])-1] = int(query[2])
        else:
            print(A[int(query[1])-1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 8

def main():
    # Write code here
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 9

def main():
    #Read input
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]

    #Process queries
    for q in query:
        if q[0] == 1:
            A[q[1]-1] = q[2]
        else:
            print(A[q[1]-1])
