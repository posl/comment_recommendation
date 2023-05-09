Synthesizing 10/10 solutions

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
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        count = 0
        for j in range(l-1, r):
            if a[j] == x:
                count += 1
        print(count)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    lr = [list(map(int, input().split())) for _ in range(q)]
    for i in range(q):
        l = lr[i][0]
        r = lr[i][1]
        x = lr[i][2]
        print(a[l-1:r].count(x))

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(_) for _ in input().split()]
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append([int(_) for _ in input().split()])

    for query in queries:
        l, r, x = query
        print(a[l-1:r].count(x))

=======
Suggestion 9

def solve(N, A, Q, queries):
    ans = []
    for q in queries:
        L, R, X = q
        ans.append(A[L-1:R].count(X))
    return ans

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
