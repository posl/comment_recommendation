Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print("是")
    else:
        print("否")

=======
Suggestion 2

def judge_polygon(n, l):
    l.sort()
    l.reverse()
    #print(l)
    if l[0] >= sum(l[1:]):
        return "否"
    else:
        return "是"

n = int(input())
l = list(map(int, input().split()))
print(judge_polygon(n, l))

=======
Suggestion 3

def is_polygon(n, l):
    if n < 3 or n > 10:
        return False

    max_l = max(l)
    sum_l = sum(l) - max_l
    if max_l < sum_l:
        return True
    else:
        return False

=======
Suggestion 4

def check_polygon(L):
    max_L = max(L)
    sum_L = sum(L)
    if max_L < sum_L - max_L:
        return "是"
    else:
        return "否"

=======
Suggestion 5

def judgePolygon(L):
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        return "是"
    else:
        return "否"

=======
Suggestion 6

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        print('是')
    else:
        print('否')

=======
Suggestion 7

def is_polygon(n, l):
    sum = 0
    max = 0
    for i in range(n):
        sum += l[i]
        if l[i] > max:
            max = l[i]
    if max < sum - max:
        return "是"
    else:
        return "否"

=======
Suggestion 8

def is_polygon(n, ls):
    ls.sort()
    if ls[-1] < sum(ls[:-1]):
        return '是'
    else:
        return '否'

=======
Suggestion 9

def check_polygon(n, l):
    sum = 0
    max = 0
    for i in range(n):
        if l[i] > max:
            max = l[i]
        sum += l[i]
    if max < sum - max:
        print("是")
    else:
        print("否")

=======
Suggestion 10

def main():
    n = int(input())
    l = list(map(int, input().split()))
    max_l = max(l)
    if max_l < sum(l) - max_l:
        print('是')
    else:
        print('否')
