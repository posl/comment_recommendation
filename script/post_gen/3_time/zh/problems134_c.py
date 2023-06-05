Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        max = 0
        for j in range(n):
            if i != j and a[j] > max:
                max = a[j]
        print(max)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        print(max(A[:i]+A[i+1:]))

=======
Suggestion 3

def main():
    # 读取输入
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    # 求解并输出
    for i in range(N):
        print(max(A[0:i] + A[i+1:N]))

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            a[i] = -1
    a_max = max(a)
    for i in range(n):
        if a[i] == -1:
            print(a_max)
        else:
            print(a_max)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A.sort()
    for i in range(N):
        if A[i] != A[N-1]:
            print(A[N-1])
        else:
            print(A[N-2])

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(max(a[:i]+a[i+1:]))
        else:
            print(max_a)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_max_index = a.index(a_max)
    a.pop(a_max_index)
    for i in range(n-1):
        print(a_max)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    max_num = max(a)
    for i in range(n):
        if a[i] == max_num:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_num)
