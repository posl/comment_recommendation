Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def delete_and_append(list):
    list.pop(0)
    list.append(0)
    return list

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

def problems278_a():
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = list(map(int,input().split()))
    #print(N, K, A)
    for i in range(K):
        A.pop(0)
        A.append(0)
    for i in range(N):
        if i == N-1:
            print(A[i])
        else:
            print(A[i], end=" ")

problems278_a()

=======
Suggestion 4

def main():
    a = []
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end = ' ')

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(" ".join(map(str, a)))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(' '.join(map(str,a)))

=======
Suggestion 8

def main():
    # 读取数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 执行操作
    for i in range(k):
        a.pop(0)
        a.append(0)
    # 打印结果
    print(' '.join(map(str, a)))

=======
Suggestion 9

def problems278_a():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

problems278_a()
