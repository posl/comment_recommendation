Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x > y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x < y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    # 读取输入
    x, y = map(int, input().split())
    # 处理
    if x < y:
        x, y = y, x
    # 输出
    if x - y < 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    x,y = input().split()
    if int(x) > int(y):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def calc(x, y):
    if x > y:
        return False
    else:
        return True

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    if X > Y:
        if X - Y < 3:
            print("Yes")
        else:
            print("No")
    else:
        if Y - X < 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def isWin(x,y):
    if x>y:
        return True
    else:
        return False
