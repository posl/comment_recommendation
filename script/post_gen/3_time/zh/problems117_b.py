Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l_max = max(l)
    l_sum = sum(l) - l_max
    if l_max < l_sum:
        print("是")
    else:
        print("否")

=======
Suggestion 2

def is_polygon(n, l):
    max_l = max(l)
    if max_l < sum(l) - max_l:
        return "是"
    else:
        return "否"

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print('是')
    else:
        print('否')

=======
Suggestion 4

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print('是')
    else:
        print('否')

=======
Suggestion 5

def check_polygon(n, l):
    # 判断是否可以画出多边形
    if n < 3 or n > 10:
        return False
    if len(l) != n:
        return False
    if any([li < 1 or li > 100 for li in l]):
        return False

    # 从大到小排序
    l.sort(reverse=True)
    # 最大边长
    max_len = l[0]
    # 其他边长之和
    other_len = sum(l[1:])
    if max_len < other_len:
        return True
    else:
        return False

=======
Suggestion 6

def is_polygon(n, l):
    l.sort()
    if l[-1] >= sum(l[:-1]):
        return False
    else:
        return True

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    # 读取输入
    n = int(input())
    l_list = list(map(int, input().split()))

    # 排序
    l_list.sort()

    # 判断
    if l_list[-1] < sum(l_list[:-1]):
        print('是')
    else:
        print('否')

=======
Suggestion 9

def is_polygon(n, l):
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        return True
    else:
        return False

=======
Suggestion 10

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print('是')
    else:
        print('否')
