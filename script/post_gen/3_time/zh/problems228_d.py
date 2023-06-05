Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

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
Suggestion 3

def init():
    global N
    N = 2 ** 20
    global A
    A = [-1] * N

=======
Suggestion 4

def main():
    N = 1048576
    A = [-1] * N
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

=======
Suggestion 5

def main():
    N = 2 ** 20
    A = [-1] * N
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

=======
Suggestion 6

def solve():
    N = 2**20
    A = [-1 for _ in range(N)]
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
Suggestion 7

def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

main()

=======
Suggestion 8

def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

=======
Suggestion 9

def main():
    # 读入数据
    n = int(input())
    # 用于存储结果
    queue = []
    # 用于存储A
    list_a = [-1 for i in range(2 ** 20)]
    # 用于存储h
    list_h = [-1 for i in range(2 ** 20)]
    # 用于存储x
    list_x = [-1 for i in range(2 ** 20)]
    # 用于存储t
    list_t = [-1 for i in range(2 ** 20)]
    for i in range(n):
        # 读入t和x
        t, x = map(int, input().split())
        list_t[i] = t
        list_x[i] = x
        # 如果t为1
        if t == 1:
            # 定义一个整数h为h=x_i。
            h = x
            # 当A_{h mod N}≠-1时，不断向h加1。我们可以证明，在这个问题的约束条件下，这个过程在有限迭代后结束。
            while list_a[h % (2 ** 20)] != -1:
                h += 1
            # 用x_i替换A_{h mod N}的值。
            list_a[h % (2 ** 20)] = x
            list_h[h % (2 ** 20)] = x
        # 如果t为2
        else:
            # 打印当时的A_{x_i mod N}的值。
            queue.append(list_a[x % (2 ** 20)])
    # 打印结果
    for i in queue:
        print(i)
