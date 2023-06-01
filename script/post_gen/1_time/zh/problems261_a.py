Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    l1,r1,l2,r2 = map(int,input().split())
    # 求解
    if r1 < l2 or r2 < l1:
        # 没有重叠
        print(0)
    else:
        # 有重叠
        print(min(r1,r2)-max(l1,l2))

=======
Suggestion 2

def problems261_a():
    l1,r1,l2,r2 = map(int,input().split())
    if r1 <= l2:
        print(0)
    elif r2 <= l1:
        print(0)
    elif l1 <= l2 and r2 <= r1:
        print(r2 - l2)
    elif l2 <= l1 and r1 <= r2:
        print(r1 - l1)
    elif l1 <= l2 and r1 <= r2:
        print(r1 - l2)
    elif l2 <= l1 and r2 <= r1:
        print(r2 - l1)

=======
Suggestion 3

def main():
    l1,r1,l2,r2=map(int,input().split())
    if l2<r1:
        print(max(l2,r1)-min(l1,r2))
    else:
        print(0)

=======
Suggestion 4

def solve():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1:
        print(max(0, min(r1, r2) - l2))
    else:
        print(0)

=======
Suggestion 5

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if (l1 <= l2 <= r1) and (r1 <= r2):
        print(r1 - l2)
    elif (l2 <= l1 <= r2) and (r2 <= r1):
        print(r2 - l1)
    elif (l1 <= l2 <= r2) and (r2 <= r1):
        print(r2 - l2)
    elif (l2 <= l1 <= r1) and (r1 <= r2):
        print(r1 - l1)
    else:
        print(0)

=======
Suggestion 6

def main():
    l_1, r_1, l_2, r_2 = map(int, input().split())
    if l_2 > r_1 or l_1 > r_2:
        print(0)
    elif l_1 <= l_2 and r_1 <= r_2:
        print(r_1 - l_2)
    elif l_2 <= l_1 and r_2 <= r_1:
        print(r_2 - l_1)
    elif l_1 <= l_2 and r_2 <= r_1:
        print(r_2 - l_2)
    elif l_2 <= l_1 and r_1 <= r_2:
        print(r_1 - l_1)
    else:
        print(0)

=======
Suggestion 7

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l2 <= l1 <= r2 <= r1:
        print(r2-l1)
    elif l1 <= l2 <= r1 <= r2:
        print(r1-l2)
    elif l1 <= l2 <= r2 <= r1:
        print(r2-l2)
    elif l2 <= l1 <= r1 <= r2:
        print(r1-l1)
    else:
        print(0)

=======
Suggestion 8

def main():
    l1,r1,l2,r2 = map(int,input().split())

    if r2 < l1 or r1 < l2:
        print(0)
    else:
        print(min(r1,r2) - max(l1,l2))

=======
Suggestion 9

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 <= l2 and l2 <= r1:
        if r1 <= r2:
            print(r1 - l2)
        else:
            print(r2 - l2)
    elif l1 <= r2 and r2 <= r1:
        if r1 <= l2:
            print(r2 - l1)
        else:
            print(r2 - l1)
    else:
        print(0)

=======
Suggestion 10

def get_length(l1, r1, l2, r2):
    if (r1 < l2) or (r2 < l1):
        return 0
    else:
        return min(r1, r2) - max(l1, l2)
