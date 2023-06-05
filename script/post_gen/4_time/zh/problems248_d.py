Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    # N = int(input())
    # A = list(map(int, input().split()))
    # Q = int(input())
    # for _ in range(Q):
    #     L,

=======
Suggestion 2

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    return N, A, Q, Query

=======
Suggestion 3

def count_num(arr, l, r, x):
    count = 0
    for i in range(l-1, r):
        if arr[i] == x:
            count += 1
    return count

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l,r,x = map(int, input().split())
        count = 0
        for j in range(l-1,r):
            if a[j] == x:
                count += 1
        print(count)

=======
Suggestion 6

def countNums(L, R, X, A):
    count = 0
    for i in range(L-1, R):
        if A[i] == X:
            count += 1
    return count

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    L, R, X = map(int, input().split())
    print(countNums(L, R, X, A))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L - 1:R].count(X))
