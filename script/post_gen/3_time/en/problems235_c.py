Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
                if count == k:
                    print(j+1)
                    break
        else:
            print(-1)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(n):
            if a[i] == x:
                cnt += 1
                if cnt == k:
                    print(i+1)
                    break
        else:
            print(-1)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        count = 0
        for i in range(N):
            if A[i] == x:
                count += 1
                if count == k:
                    print(i+1)
                    break
        else:
            print(-1)

=======
Suggestion 5

def get_input():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        x, k = map(int, input().split())
        queries.append((x, k))
    return n, q, a, queries

=======
Suggestion 6

def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        x, k = map(int, input().split())
        queries.append((x, k))
    return N, Q, A, queries

=======
Suggestion 7

def get_input():
    n, q = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split(' '))))
    return n, q, a, queries

=======
Suggestion 8

def find_kth_occurrence(a, x, k):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                return i + 1
    return -1

=======
Suggestion 9

def find_kth_occurrence(arr, k, x):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

=======
Suggestion 10

def process_query(arr, x, k):
    """
    :param arr: array of integers
    :param x: integer
    :param k: integer
    :return: index of k-th occurrence of x in arr
    """
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1
