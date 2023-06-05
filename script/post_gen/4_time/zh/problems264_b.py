Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    if R % 2 == 1:
        if C % 2 == 1:
            print("黑色")
        else:
            print("白色")
    else:
        if C % 2 == 1:
            print("白色")
        else:
            print("黑色")

=======
Suggestion 2

def main():
    # 读取输入
    r, c = map(int, input().split())
    # 判断是否为黑色
    if (r+c)%2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 3

def print_color(row, col):
    if row % 2 == 0:
        if col % 2 == 0:
            print("白色")
        else:
            print("黑色")
    else:
        if col % 2 == 0:
            print("黑色")
        else:
            print("白色")

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print("白色")
        else:
            print("黑色")
    else:
        if C % 2 == 0:
            print("黑色")
        else:
            print("白色")

=======
Suggestion 5

def main():
    R,C = map(int,input().split())
    if (R+C)%2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 6

def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print('白色')
        else:
            print('黑色')
    else:
        if C % 2 == 0:
            print('黑色')
        else:
            print('白色')

=======
Suggestion 7

def main():
    # 读取输入
    R, C = map(int, input().strip().split())
    # 处理
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 8

def main():
    r, c = map(int, input().split())
    if r % 2 == 0:
        if c % 2 == 0:
            print("black")
        else:
            print("white")
    else:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
