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

=======
Suggestion 2

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

=======
Suggestion 3

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
Suggestion 4

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
        else:
            print(a[query[1] - 1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        x = list(map(int, input().split()))
        if x[0] == 1:
            for j in range(n):
                a[j] = x[1]
        elif x[0] == 2:
            a[x[1] - 1] += x[2]
        else:
            print(a[x[1] - 1])

=======
Suggestion 6

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    return N, A, Q, query

=======
Suggestion 7

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
        else:
            print(a[query[1] - 1])

main()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            for i in range(n):
                a[i] = x
        elif query[0] == '2':
            i, x = int(query[1]), int(query[2])
            a[i-1] += x
        else:
            i = int(query[1])
            print(a[i-1])

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(i) for i in input().split()])
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(N):
                A[j] = query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        elif query[i][0] == 3:
            print(A[query[i][1]-1])

=======
Suggestion 10

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
