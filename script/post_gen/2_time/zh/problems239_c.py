Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_distance_5(x1, y1, x2, y2):
    if (x1 == x2 and y1 == y2):
        return False
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) == 5:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    x1,y1,x2,y2=map(int,input().split())
    if (x1-x2)**2+(y1-y2)**2==5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def problems239_c():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 == 5:
        print('Yes')
    elif ((x1 - x2) ** 2 + (y1 - y2 - 1) ** 2) ** 0.5 == 5:
        print('Yes')
    elif ((x1 - x2) ** 2 + (y1 - y2 + 1) ** 2) ** 0.5 == 5:
        print('Yes')
    elif ((x1 - x2 - 1) ** 2 + (y1 - y2) ** 2) ** 0.5 == 5:
        print('Yes')
    elif ((x1 - x2 + 1) ** 2 + (y1 - y2) ** 2) ** 0.5 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 10:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if (x_1-x_2)**2 + (y_1-y_2)**2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1-x2)**2+(y1-y2)**2==5:
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 7

def judge(x1,y1,x2,y2):
    if (x1-x2)**2+(y1-y2)**2==5:
        return True
    else:
        return False

x1,y1,x2,y2=map(int,input().split())

=======
Suggestion 8

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if (x1-x2)**2+(y1-y2)**2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    # 读取输入
    x1, y1, x2, y2 = map(int, input().split())
    # 判断是否满足条件
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")
