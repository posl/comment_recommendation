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
            for i in range(n):
                a[i] = query[1]
        elif query[0] == 2:
            a[query[1]-1] += query[2]
        else:
            print(a[query[1]-1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    query.reverse()
    for i in range(q):
        if query[i][0] == 1:
            for j in range(n):
                a[j] = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        else:
            print(a[query[i][1]-1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        s = input().split()
        if s[0] == '1':
            for i in range(n):
                a[i] = int(s[1])
        elif s[0] == '2':
            a[int(s[1])-1] += int(s[2])
        else:
            print(a[int(s[1])-1])

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
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        s = input().split()
        if s[0] == '1':
            x = int(s[1])
            for j in range(N):
                A[j] = x
        elif s[0] == '2':
            i = int(s[1]) - 1
            x = int(s[2])
            A[i] += x
        else:
            i = int(s[1]) - 1
            print(A[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(j) for j in input().split()])

    for query in queries:
        if query[0] == 1:
            for i in range(N):
                A[i] = query[1]
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])
