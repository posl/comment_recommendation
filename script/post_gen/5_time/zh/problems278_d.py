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
            for j in range(N):
                A[j] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        else:
            print(A[query[1]-1])
    return 0

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
            a[query[1] - 1] += query[2]
        elif query[0] == 3:
            print(a[query[1] - 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for i in range(N):
                A[i] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        elif query[0] == 3:
            print(A[query[1]-1])

=======
Suggestion 4

def problem278d():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))

    # print(N)
    # print(A)
    # print(Q)
    # print(queries)

    for q in queries:
        if q[0] == 1:
            for i in range(N):
                A[i] = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 1. 二分探索で該当するindexを探す
    # 2. 二分探索で該当するindexを探す
    # 3. 二分探索で該当するindexを探す
    # 4. 二分探索で該当するindexを探す
    # 5. 二分探索で該当するindexを探す
    # 6. 二分探索で該当するindexを探す
    # 7. 二分探索で該当するindexを探す
    # 8. 二分探索で該当するindexを探す
    # 9. 二分探索で該当するindexを探す
    # 10. 二分探索で該当するindexを探す

    # 1. 二分探索で該当するindexを探す
    # 2. 二分探索で該当するindexを探す
    # 3. 二分探索で該当するindexを探す
    # 4. 二分探索で該当するindexを探す
    # 5. 二分探索で該当するindexを探す
    # 6. 二分探索で該当するindexを探す
    # 7. 二分探索で該当するindexを探す
    # 8. 二分探索で該当するindexを探す
    # 9. 二分探索で該当するindexを探す
    # 10. 二分探索で該当するindexを探す

    # 1. 二分探索で該当するindex

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    queries.reverse()
    for query in queries:
        if query[0] == 1:
            A = list(map(lambda x: query[1], A))
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    query = [input().split() for _ in range(q)]
    #print(query)
    #print(a)
    for i in query:
        if i[0] == '1':
            a = [int(i[1]) for _ in range(n)]
        elif i[0] == '2':
            a[int(i[1])-1] += int(i[2])
        else:
            print(a[int(i[1])-1])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a = [query[1] for _ in range(n)]
        elif query[0] == 2:
            a[query[1]-1] += query[2]
        else:
            print(a[query[1]-1])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            for i in range(len(A)):
                A[i] = x
        elif query[0] == '2':
            i = int(query[1])
            x = int(query[2])
            A[i-1] += x
        else:
            i = int(query[1])
            print(A[i-1])
