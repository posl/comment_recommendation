Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if (x1-x2)**2 + (y1-y2)**2 == 10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # 读取输入
    x1, y1, x2, y2 = map(int, input().split())
    # 两点距离
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    # 判断是否为整数
    if dist.is_integer():
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def is_5_2(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return False
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        return True
    else:
        return False

=======
Suggestion 4

def main():
    # x_1, y_1, x_2, y_2 = map(int, input().split())
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    # if x_1 == x_2 and y_1 == y_2:
    #     print("No")
    #     return
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if x_1 == x_2 and y_1 == y_2:
        print("No")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 10:
        print("Yes")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 25:
        print("Yes")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) == (5)**(1/2) or ((x1 - y2)**2 + (y1 - x2)**2)**(1/2) == (5)**(1/2):
        print("Yes")
    else:
        print("No")
