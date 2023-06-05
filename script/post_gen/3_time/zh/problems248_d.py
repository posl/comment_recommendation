Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    for _ in range(Q):
        L, R, X = [int(x) for x in input().split()]
        print(A[L-1:R].count(X))

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

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    return n, a, q, query

=======
Suggestion 4

def countNum(arr, l, r, x):
    count = 0
    for i in range(l-1, r):
        if arr[i] == x:
            count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
for i in range(q):
    l, r, x = map(int, input().split())
    print(countNum(arr, l, r, x))

=======
Suggestion 5

def findNums(L,R,X):
    count = 0
    for i in range(L-1,R):
        if A[i] == X:
            count += 1
    return count

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 7

def find_num(arr,l,r,x):
    count = 0
    for i in range(l-1,r):
        if arr[i] == x:
            count += 1
    return count

=======
Suggestion 8

def count(arr, l, r, x):
    count = 0
    for i in range(l-1, r):
        if arr[i] == x:
            count += 1
    return count

=======
Suggestion 9

def solve():
    pass

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))
