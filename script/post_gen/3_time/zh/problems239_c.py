Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_square(n):
    return n**0.5 == int(n**0.5)

x1,y1,x2,y2 = map(int,input().split())

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1-x2)**2 + (y1-y2)**2)**0.5 == (5**0.5):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    x1,y1,x2,y2 = map(int, input().split())
    if (x1,y1) == (x2,y2):
        print("No")
        return
    elif abs(x1-x2) == abs(y1-y2):
        print("Yes")
        return
    else:
        print("No")
        return

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print('No')
    else:
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if (x2 - x1)**2 + (y2 - y1)**2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # 读取输入
    x1, y1, x2, y2 = map(int, input().split())
    # 计算两点间的距离
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 判断距离是否等于根号5
    if dist == 5 ** 0.5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if(x1 == x2 and y1 == y2):
        print('No')
        return
    if(x1 == x2):
        if(abs(y1-y2) == 5):
            print('Yes')
            return
        else:
            print('No')
            return
    if(y1 == y2):
        if(abs(x1-x2) == 5):
            print('Yes')
            return
        else:
            print('No')
            return
    if(abs(x1-x2) == 5 and abs(y1-y2) == 5):
        print('Yes')
        return
    else:
        print('No')
        return

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return

    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
        return

    if (x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2):
        print("Yes")
        return

    print("No")

=======
Suggestion 9

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if (x1-x2)**2+(y1-y2)**2 == 10:
        print("Yes")
    else:
        print("No")
