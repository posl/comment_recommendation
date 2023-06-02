Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(' '.join(map(str, A)))

=======
Suggestion 2

def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = input().split()
    for k in range(K):
        A.pop(0)
        A.append('0')
    print(' '.join(A))

=======
Suggestion 3

def problem278_a():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(K):
        A.append(0)
        A.pop(0)
    print(*A)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=" ")

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(" ".join(map(str, A)))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(*A)

=======
Suggestion 9

def main():
    #输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #处理
    for i in range(k):
        a.pop(0)
        a.append(0)
    #输出
    print(" ".join(map(str, a)))
