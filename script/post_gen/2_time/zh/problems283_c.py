Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def processQuery(q):
    if q[0] == 1:
        A[q[1]] = q[2]
    elif q[0] == 2:
        print(A[q[1]])

N = int(input())
A = [0] + list(map(int, input().split()))
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

for q in query:
    processQuery(q)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))

    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1]-1] = query[i][2]
        else:
            print(A[query[i][1]-1])

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        cmd = list(map(int,input().split()))
        if cmd[0] == 1:
            a[cmd[1]-1] = cmd[2]
        elif cmd[0] == 2:
            print(a[cmd[1]-1])

=======
Suggestion 5

def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        elif query[0] == 2:
            print(A[query[1]-1])

=======
Suggestion 6

def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    # 依次处理查询
    for _ in range(q):
        query = list(map(int, input().split()))
        # 查询类型1
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        # 查询类型2
        else:
            print(a[query[1] - 1])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        s = input().split()
        if s[0] == '1':
            a[int(s[1]) - 1] = int(s[2])
        else:
            print(a[int(s[1]) - 1])

=======
Suggestion 8

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
Suggestion 9

def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    #处理
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])
