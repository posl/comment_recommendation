Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        elif query[0] == 2:
            print(a[query[1] - 1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        else:
            print(a[query[1]-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A[q[1]-1] = q[2]
        else:
            print(A[q[1]-1])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A[q[1]-1] = q[2]
        elif q[0] == 2:
            print(A[q[1]-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        b = list(map(int, input().split()))
        if b[0] == 1:
            a[b[1]-1] = b[2]
        else:
            print(a[b[1]-1])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        b = list(map(int, input().split()))
        if b[0] == 1:
            a[b[1] - 1] = b[2]
        elif b[0] == 2:
            print(a[b[1] - 1])

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    for i in range(q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        elif query[0] == 2:
            print(a[query[1] - 1])
        else:
            print("Error: Invalid query type")
    return

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            a[l[1] - 1] = l[2]
        else:
            print(a[l[1] - 1])

=======
Suggestion 9

def solution(input):
    n = input[0]
    a = input[1]
    q = input[2]
    for i in range(q):
        if input[3 + i][0] == 1:
            a[input[3 + i][1] - 1] = input[3 + i][2]
        else:
            print(a[input[3 + i][1] - 1])
