Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    return n, a, q, query

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        count = 0
        for i in range(L-1, R):
            if A[i] == X:
                count += 1
        print(count)

=======
Suggestion 4

def getinput():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    return n, a, q, query

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 6

def count_element(start, end, x):
    count = 0
    for i in range(start, end+1):
        if a[i] == x:
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    l, r, x = map(int, input().split())
    print(count_element(l-1, r-1, x))

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
        l = query[0] - 1
        r = query[1]
        x = query[2]
        print(a[l:r].count(x))

=======
Suggestion 8

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
Suggestion 9

def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    L, R, X = map(int, input().split())
    print(binary_search(A, L - 1, R - 1, X))
