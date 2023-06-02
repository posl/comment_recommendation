Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for i in range(Q)]
    a = [i+1 for i in range(N)]
    for i in range(Q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(*a)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N + 1)]
    for i in range(Q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(*a)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    #print(x)
    a = [i for i in range(1, n+1)]
    #print(a)
    for i in range(q):
        #print(x[i])
        #print(a)
        #print(a.index(x[i]))
        tmp = a.index(x[i])
        #print(tmp)
        if tmp != n-1:
            a[tmp], a[tmp+1] = a[tmp+1], a[tmp]
        else:
            a[tmp], a[tmp-1] = a[tmp-1], a[tmp]
    #print(a)
    print(*a)

=======
Suggestion 4

def swap(x, i):
    if x[i] == i + 1:
        return x
    else:
        tmp = x[i]
        x[i] = x[i + 1]
        x[i + 1] = tmp
        return x

=======
Suggestion 5

def main():
    import sys
    # 读取标准输入
    lines = sys.stdin.readlines()
    # 读取第一行
    line = lines[0].strip()
    # 按空格分割
    n, q = line.split()
    # 转换为整数
    n = int(n)
    q = int(q)
    # 读取第二行
    line = lines[1].strip()
    # 按空格分割
    x = line.split()
    # 转换为整数
    x = [int(i) for i in x]
    # 球的位置
    pos = [i for i in range(1, n + 1)]
    # 操作
    for i in range(q):
        # 球的位置
        p = pos[x[i] - 1]
        # 球的位置
        pos[x[i] - 1] = pos[x[i]]
        # 球的位置
        pos[x[i]] = p
        # 球的位置
        x[i] = x[i] + 1
    # 打印
    for i in range(n):
        print(pos[i], end=" ")

=======
Suggestion 6

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

=======
Suggestion 7

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

=======
Suggestion 8

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

=======
Suggestion 9

def main():
    # 读取数据
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    # 初始化
    a = [i for i in range(1, n+1)]
    # 交换
    for i in range(q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    # 输出
    print(' '.join(map(str, a)))

=======
Suggestion 10

def swap(arr, i, j):
    if i == j:
        return
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
