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
            for j in range(N):
                A[j] = query[1]
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
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))

    # 初始值
    sum = 0
    for i in range(n):
        sum += a[i]

    # 处理
    for query in queries:
        if query[0] == 1:
            sum += query[1] * n
        elif query[0] == 2:
            sum += query[2]
        else:
            print(sum)

=======
Suggestion 3

def sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            for i in range(N):
                A[i] = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])
    return 0

=======
Suggestion 5

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
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 6

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
        elif query[0] == 3:
            print(a[query[1]-1])

=======
Suggestion 7

def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(n):
                A[j] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        elif query[0] == 3:
            print(A[query[1]-1])

=======
Suggestion 8

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
        else:
            print(A[query[i][1]-1])
