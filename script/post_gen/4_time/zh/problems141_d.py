Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, m, a):
    a.sort()
    for i in range(m):
        a[-1] = a[-1] // 2
        a.sort()
    return sum(a)

=======
Suggestion 2

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0]//2
        a.sort(reverse=True)
    return sum(a)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 4

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(m):
        a[-1]=a[-1]//2
        a.sort()
    print(sum(a))

=======
Suggestion 5

def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

=======
Suggestion 6

def problem141_d():
    pass

=======
Suggestion 7

def solve(n, m, a):
    a = sorted(a, reverse = True)
    i = 0
    while i < m and a[i] >= a[0] / (2 ** (i + 1)):
        i += 1
    return sum(a[i:]) + sum([a[0] / (2 ** (i + 1)) for i in range(i)])

=======
Suggestion 8

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 逐个处理
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        if a[0] < a[1]:
            a[0], a[1] = a[1], a[0]
    # 输出答案
    print(sum(a))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(m):
        a[n-1] = a[n-1]//2
        a.sort()
    print(sum(a))
