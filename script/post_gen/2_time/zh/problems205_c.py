Synthesizing 10/10 solutions

=======
Suggestion 1

def is_permutation(array):
    # 从小到大排序
    array.sort()
    # 检查是否为1到N的连续数列
    for i in range(len(array)):
        if array[i] != i + 1:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

=======
Suggestion 2

def is_permutation(n, a):
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            return False
    return True

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == [i for i in range(1, n+1)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def is_permutation(n, a):
    if len(a) != n:
        return False
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            return False
    return True

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if(A == list(range(1,N+1))):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check_permutation(N, A):
    if N != len(A):
        return False
    else:
        for i in range(N):
            if i+1 not in A:
                return False
        return True

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if set(A) == set(range(1, N+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))

    # 逻辑处理
    A.sort()
    if A == list(range(1, N + 1)):
        print('Yes')
    else:
        print('No')
