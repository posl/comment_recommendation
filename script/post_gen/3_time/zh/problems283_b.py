Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
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
            a[query[1] - 1] = query[2]
        else:
            print(a[query[1] - 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A[q[1] - 1] = q[2]
        elif q[0] == 2:
            print(A[q[1] - 1])

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    for i in range(Q):
        q = list(map(int,input().split()))
        if q[0] == 1:
            A[q[1]-1] = q[2]
        else:
            print(A[q[1]-1])

main()  #AC

=======
Suggestion 6

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            arr[q[1] - 1] = q[2]
        else:
            print(arr[q[1] - 1])

=======
Suggestion 7

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            A[int(query[1])-1] = int(query[2])
        elif query[0] == '2':
            print(A[int(query[1])-1])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        b = list(map(int, input().split()))
        if b[0] == 1:
            a[b[1] - 1] = b[2]
        else:
            print(a[b[1] - 1])

=======
Suggestion 10

def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    # 处理查询
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])
