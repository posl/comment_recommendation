Synthesizing 10/10 solutions

=======
Suggestion 1

def process():
    N = 1048576
    A = [-1] * (N + 1)
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
process()

=======
Suggestion 2

def main():
    import sys
    readline = sys.stdin.readline
    N = 2 ** 20
    A = [-1] * N
    Q = int(readline())
    for _ in range(Q):
        t, x = map(int, readline().split())
        if t == 1:
            while A[x % N] != -1:
                x += 1
            A[x % N] = x
        else:
            print(A[x % N])

=======
Suggestion 3

def main():
    N = 2**20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 4

def main():
    n = 2**20
    q = int(input())
    a = [-1]*n
    for _ in range(q):
        t, x = map(int, input().split())
        x = x % n
        if t == 1:
            while a[x] != -1:
                x += 1
                x = x % n
            a[x] = x
        else:
            print(a[x])

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    # 获取输入内容
    q = int(input())
    # 定义列表
    a = [-1 for i in range(2 ** 20)]
    # 循环处理输入内容
    for i in range(q):
        # 获取输入内容
        t, x = map(int, input().split())
        # 判断输入内容
        if t == 1:
            # 定义变量
            h = x
            # 循环处理
            while a[h % (2 ** 20)] != -1:
                h += 1
            # 定义变量
            a[h % (2 ** 20)] = x
        else:
            # 输出结果
            print(a[x % (2 ** 20)])

=======
Suggestion 7

def solve():
    N = 2 ** 20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])
solve()

=======
Suggestion 8

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = 2 ** 20
    Q = int(input())
    A = [-1] * N
    q = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
            q.append(h % N)
        else:
            if x <= q[0]:
                print(A[x])
            else:
                print(-1)

=======
Suggestion 9

def main():
    # 读入数据
    Q = int(input())
    # 用字典存储数据
    A = {}
    # 用列表存储查询
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # 处理查询
    for i in range(Q):
        if query[i][0] == 1:
            h = query[i][1]
            while A.get(h % 1048576) != None:
                h += 1
            A[h % 1048576] = query[i][1]
        else:
            print(A.get(query[i][1] % 1048576))

=======
Suggestion 10

def main():
    Q = int(input())
    A = [-1] * (2 ** 20)
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % (2 ** 20)] != -1:
                h += 1
            A[h % (2 ** 20)] = x
        else:
            print(A[x % (2 ** 20)])
