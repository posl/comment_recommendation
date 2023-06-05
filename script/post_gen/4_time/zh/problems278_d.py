Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            for j in range(n):
                a[j] = int(query[1])
        elif query[0] == '2':
            a[int(query[1]) - 1] += int(query[2])
        else:
            print(a[int(query[1]) - 1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for i in range(n):
                a[i] = query[1]
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
    ans = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ans += query[1]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        else:
            print(a[query[1] - 1] + ans)
main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(N):
                A[j] = query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        elif query[i][0] == 3:
            print(A[query[i][1]-1])

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    #print(N, A, Q, query)
    for q in query:
        if q[0] == 1:
            for i in range(N):
                A[i] = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a = [query[1] for _ in range(n)]
        elif query[0] == 2:
            a[query[1] - 1] += query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    # print(N)
    # print(A)
    # print(Q)
    # print(query)

    # for q in query:
    #     if q[0] == 1:
    #         for i in range(N):
    #             A[i] = q[1]
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])

    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1] for _ in range(N)]
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])

    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])

    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])

    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-1] += q[2]
    #     else:
    #         print(A[q[1]-1])

    # for q in query:
    #     if q[0] == 1:
    #         A = [q[1]] * N
    #     elif q[0] == 2:
    #         A[q[1]-

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] == 1:
            for i in range(n):
                a[i] = query[1]
        elif query[0] == 2:
            a[query[1]-1] += query[2]
        elif query[0] == 3:
            print(a[query[1]-1])
