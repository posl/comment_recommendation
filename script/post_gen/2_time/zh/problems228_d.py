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

def main():
    # 读入输入
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))

    # 用于存储结果
    result = []

    # 用于存储序列A
    A = [-1 for i in range(2 ** 20)]

    # 处理查询
    for i in range(q):
        if query[i][0] == 1:
            h = query[i][1]
            while A[h % (2 ** 20)] != -1:
                h += 1
            A[h % (2 ** 20)] = query[i][1]
        else:
            result.append(A[query[i][1] % (2 ** 20)])

    # 输出结果
    for i in range(len(result)):
        print(result[i])

=======
Suggestion 4

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
Suggestion 5

def main():
    N = 2 ** 20
    A = [-1 for i in range(N)]
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        elif t == 2:
            print(A[x % N])
