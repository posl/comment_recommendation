Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(" ".join(map(str, a)))

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(k):
        a.append(0)
        a.pop(0)

    print(' '.join(map(str, a)))

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    for i in range(N):
        if i == N-1:
            print(A[i])
        else:
            print(A[i],end=' ')

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(k):
        a.pop(0)
        a.append(0)

    for i in range(n):
        print(a[i], end=' ')

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[k:] + [0] * k
    print(*a)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    for i in range(N):
        print(A[i], end=' ')
    print()

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

solve()

=======
Suggestion 9

def main():
    # 读取数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 执行k次操作
    for i in range(k):
        # 删除第一个元素
        a.pop(0)
        # 在末尾添加0
        a.append(0)
    # 输出结果
    print(*a)

=======
Suggestion 10

def move(a):
    a.pop(0)
    a.append(0)
    return a
