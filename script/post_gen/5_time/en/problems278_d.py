Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A = [query[1] for _ in range(N)]
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(n):
                a[j] = query[1]
        elif query[0] == 2:
            a[query[1]-1] += query[2]
        else:
            print(a[query[1]-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0]==1:
            for i in range(N):
                A[i] = query[1]
        elif query[0]==2:
            A[query[1]-1] += query[2]
        else:
            print(A[query[1]-1])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))

    for query in queries:
        if query[0] == 1:
            A = [query[1]] * N
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))

    queries.reverse()

    for q in queries:
        if q[0] == 1:
            A = [q[1]] * N
        elif q[0] == 2:
            A[q[1] - 1] += q[2]
        else:
            print(A[q[1] - 1])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    for query in queries:
        if query[0] == 1:
            for i in range(n):
                a[i] = query[1]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int, input().split())))

    total = sum(A)
    add = 0
    for q in query:
        if q[0] == 1:
            add += q[1]
        elif q[0] == 2:
            A[q[1] - 1] += q[2]
            total += q[2]
        else:
            print(A[q[1] - 1] + add)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    for i in range(q):
        if query[i][0] == 1:
            a = [query[i][1]] * n
        elif query[i][0] == 2:
            a[query[i][1] - 1] += query[i][2]
        else:
            print(a[query[i][1] - 1])
    return

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] == 1:
            A = [query[1]] * N
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    b = [input().split() for _ in range(q)]
    for i in range(q):
        if b[i][0] == '1':
            a = [int(b[i][1]) for _ in range(n)]
        elif b[i][0] == '2':
            a[int(b[i][1])-1] += int(b[i][2])
        else:
            print(a[int(b[i][1])-1])
main()
