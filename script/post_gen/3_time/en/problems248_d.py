Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        l, r, x = map(int, input().split())
        queries.append([l, r, x])
    for query in queries:
        l = query[0]
        r = query[1]
        x = query[2]
        print(a[l-1:r].count(x))

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(i) for i in input().split()])

    for query in queries:
        L, R, X = query
        print(A[L-1:R].count(X))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    for L, R, X in queries:
        print(A[L-1:R].count(X))
