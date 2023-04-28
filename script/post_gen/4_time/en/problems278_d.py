Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            a = [x for i in range(n)]
        elif query[0] == 2:
            i = query[1]
            x = query[2]
            a[i-1] += x
        else:
            i = query[1]
            print(a[i-1])

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    for i in range(q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            a = [query[1] for x in range(n)]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    s = sum(a)
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s += query[1]*n
        elif query[0] == 2:
            s += query[1]
        else:
            print(s + a[query[1]-1])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    for q in queries:
        if q[0] == 1:
            A = [q[1]]*N
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        else:
            print(A[q[1]-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        if b[i][0] == 1:
            for j in range(n):
                a[j] = b[i][1]
        elif b[i][0] == 2:
            a[b[i][1] - 1] += b[i][2]
        elif b[i][0] == 3:
            print(a[b[i][1] - 1])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        if b[i][0] == 1:
            a = [b[i][1]] * n
        elif b[i][0] == 2:
            a[b[i][1] - 1] += b[i][2]
        else:
            print(a[b[i][1] - 1])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] == 1:
            a = [query[1] for i in range(n)]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        elif query[0] == 3:
            print(a[query[1] - 1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    S = sum(A)
    for q in queries:
        if q[0] == 1:
            S += q[1] * N
        elif q[0] == 2:
            S += q[2]
        else:
            print(A[q[1]-1] + q[1] * N)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))

    total = sum(a)
    for query in queries:
        if query[0] == 1:
            total = total + n * query[1]
        elif query[0] == 2:
            total = total - a[query[1] - 1] + query[2]
            a[query[1] - 1] = query[2]
        else:
            print(total)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    #print(N, A, Q, query)

    #print(A)
    #print(query)

    for q in query:
        #print(q)
        if q[0] == 1:
            A = [q[1] for _ in range(N)]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])
        else:
            print("ERROR")
