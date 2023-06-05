Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems278_a():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str,a)))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(' '.join(map(str, A)))

=======
Suggestion 3

def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 执行k次操作
    for i in range(k):
        # 删除a的初始元素，并在a的尾部附加一个0
        del a[0]
        a.append(0)
    # 输出结果
    print(*a)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        tmp = A.pop(0)
        A.append(tmp)
    print(" ".join(map(str, A)))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(*a)

=======
Suggestion 6

def main():
    #读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    #执行K次操作
    for _ in range(k):
        a.append(0)
        a.pop(0)

    #打印结果
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)
