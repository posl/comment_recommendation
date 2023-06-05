Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    for i in range(m):
        if a[i] < sum_a / (4 * m):
            print("否")
            break
    else:
        print("是")

=======
Suggestion 2

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    if a[m-1] * 4 * m >= sum:
        print('是')
    else:
        print('否')

=======
Suggestion 3

def get_input():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    return n,m,a

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum >= sum(a) * 0.25:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    a.sort(reverse=True)
    if a[m-1]*4*m >= sum_a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 排序
    a.sort(reverse=True)
    # 计算总票数
    total = sum(a)
    # 判断是否为受欢迎的项目
    if a[m-1] >= total / (4 * m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    a.sort(reverse=True)
    if a[m-1] >= sum_a/(4*m):
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total / (4*m):
        print('是')
    else:
        print('否')

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum >= sum(A) / (4 * M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    count = 0
    for i in range(m):
        if a[i]*4*m >= total:
            count += 1
    if count == m:
        print("是")
    else:
        print("否")
