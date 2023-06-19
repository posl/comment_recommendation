Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
        return
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(a[i]+1)
            return
    print(a[-1]+1)
    return

=======
Suggestion 2

def find_missing_number(n, a):
    a.sort()
    if a[0] != 0:
        return 0
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            return a[i - 1] + 1
    return a[n - 1] + 1

=======
Suggestion 3

def find_min_positive_integer(N, A):
    result = 0
    A.sort()
    for i in range(N):
        if A[i] > result:
            return result
        elif A[i] == result:
            result += 1
    return result

=======
Suggestion 4

def find_min_positive_int():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] > 0:
        return 0
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            return a[i-1] + 1
    else:
        return a[-1] + 1

=======
Suggestion 5

def main():
    #输入
    N = int(input())
    A = list(map(int, input().split()))
    #处理
    #排序
    A.sort()
    #去重
    A = list(set(A))
    #去零
    A = [i for i in A if i != 0]
    #输出
    print(min([i for i in range(1, 2001) if i not in A]))

=======
Suggestion 6

def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    i = 0
    while i < N:
        if i != A[i]:
            print(i)
            break
        i = i + 1
    if i == N:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] > ans:
            print(ans)
            return
        elif A[i] == ans:
            ans += 1
    print(ans)

=======
Suggestion 8

def findmin(A):
    n = len(A)
    if n == 1:
        if A[0] == 0:
            return 1
        else:
            return 0
    else:
        A.sort()
        if A[0] > 0:
            return 0
        else:
            for i in range(1, n):
                if A[i] - A[i - 1] > 1:
                    return A[i - 1] + 1
            return A[n - 1] + 1

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if a[0] != 0:
        print(0)
        return

    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print(a[i - 1] + 1)
            return

    print(a[n - 1] + 1)

=======
Suggestion 10

def f():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = []
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
    for i in range(len(b)):
        if b[i] != i:
            print(i)
            return
    print(len(b))

f()
