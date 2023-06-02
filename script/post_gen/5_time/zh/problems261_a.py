Synthesizing 10/10 solutions

=======
Suggestion 1

def cal(a,b,c,d):
    if b<=c or d<=a:
        return 0
    elif c<=a and b<=d:
        return b-a
    elif a<=c and d<=b:
        return d-c
    elif a<=c and c<=b and b<=d:
        return b-c
    elif c<=a and a<=d and d<=b:
        return d-a

=======
Suggestion 2

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 < l2:
        if r1 < l2:
            print(0)
        else:
            print(min(r1,r2) - l2)
    else:
        if r2 < l1:
            print(0)
        else:
            print(min(r1,r2) - l1)

=======
Suggestion 3

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 and l2 <= r1:
        if r2 <= r1:
            print(r2 - l2)
        else:
            print(r1 - l2)
    elif l1 <= r2 and r2 <= r1:
        if l2 >= l1:
            print(r2 - l2)
        else:
            print(r2 - l1)
    else:
        print(0)

=======
Suggestion 4

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if (l2 <= l1 and l1 <= r2) or (l2 <= r1 and l1 <= r2) or (l1 <= l2 and l2 <= r1) or (l1 <= r2 and l2 <= r1):
        print(min(r1,r2)-max(l1,l2))
    else:
        print(0)

=======
Suggestion 5

def main():
    # 读取输入
    l1, r1, l2, r2 = map(int, input().split(' '))
    # 计算
    if l2 <= l1 <= r2:
        if l2 <= r1 <= r2:
            print(r1 - l1)
        else:
            print(r2 - l1)
    elif l1 <= l2 <= r1:
        if l1 <= r2 <= r1:
            print(r2 - l2)
        else:
            print(r1 - l2)
    else:
        print(0)

=======
Suggestion 6

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l2 > r1 or l1 > r2:
        print(0)
    else:
        print(min(r1,r2) - max(l1,l2))

=======
Suggestion 7

def get_line_length(l1,r1,l2,r2):
    #两个线段不相交
    if r1 <= l2 or l1 >= r2:
        return 0
    #两个线段相交
    else:
        return min(r1,r2) - max(l1,l2)

=======
Suggestion 8

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 >= r2 or r1 <= l2:
        print(0)
    elif l1 < l2 and r1 <= r2:
        print(r1-l2)
    elif l1 >= l2 and r1 > r2:
        print(r2-l1)
    elif l1 < l2 and r1 > r2:
        print(r2-l2)
    else:
        print(r1-l1)

=======
Suggestion 9

def problem261_a():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 and l2 < r1 and r1 <= r2:
        print(r1 - l2)
    elif l1 <= l2 and l2 < r2 and r2 <= r1:
        print(r2 - l2)
    elif l2 <= l1 and l1 < r2 and r2 <= r1:
        print(r2 - l1)
    elif l2 <= l1 and l1 < r1 and r1 <= r2:
        print(r1 - l1)
    else:
        print(0)

=======
Suggestion 10

def solve():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 < l2:
        l1,l2 = l2,l1
        r1,r2 = r2,r1
    if l1 > r2:
        print(0)
    else:
        print(min(r1,r2)-l2)
