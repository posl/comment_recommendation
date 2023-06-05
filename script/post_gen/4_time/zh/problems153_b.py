Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H,N = map(int,input().split())
    A = list(map(int,input().split()))
    if sum(A) >= H:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solution(h, n, a):
    a.sort()
    for i in range(n):
        h -= a[i]
        if h <= 0:
            return "Yes"
    return "No"

=======
Suggestion 3

def solve():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    s = sum(a)
    if s >= h:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if h <= sum(a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if sum(a) >= h:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if sum(a) >= h:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # 读取输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))

    # 一开始是不行的
    can = False

    # 从大到小排序
    A.sort(reverse=True)

    # 从大到小循环
    for a in A:
        # 如果H小于a，那么就是不行的
        if H <= a:
            can = True
            break
        # 如果H大于a，那么就减去a
        else:
            H -= a

    # 打印结果
    if can:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    h,n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # 读取数据
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 处理数据
    # 输出数据
    print('Yes')
    # print('No')
