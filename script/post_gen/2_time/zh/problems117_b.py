Synthesizing 10/10 solutions

=======
Suggestion 1

def judge(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return '是'
    else:
        return '否'

=======
Suggestion 2

def judge(n, l):
    l.sort()
    if l[n-1] < sum(l[:n-1]):
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

def check_polygon(n, l):
    l.sort(reverse = True)
    if l[0] < sum(l[1:]):
        return True
    else:
        return False

=======
Suggestion 5

def main():
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    if l[-1] < sum(l[:-1]):
        print('是')
    else:
        print('否')

=======
Suggestion 6

def is_polygon(L):
    max_length = max(L)
    if max_length < sum(L)-max_length:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    maxL = max(L)
    sumL = sum(L)
    if maxL < sumL - maxL:
        print('是')
    else:
        print('否')

=======
Suggestion 8

def problem117_b():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        print("是")
    else:
        print("否")

=======
Suggestion 9

def is_drawable(n, l):
    # l.sort()
    max_l = max(l)
    sum_l = sum(l) - max_l
    return max_l < sum_l

=======
Suggestion 10

def is_polygon(n, l):
    if max(l) < sum(l) - max(l):
        return True
    else:
        return False
