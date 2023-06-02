Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取数据
    r, c = map(int, input().split())
    # 逻辑处理
    if (r + c) % 2 == 0:
        print("黑色")
    else:
        print("白色")
    # 输出结果

=======
Suggestion 2

def main():
    R,C = map(int,input().split())
    if R%2==0 and C%2==0:
        print("白色")
    elif R%2==1 and C%2==1:
        print("白色")
    else:
        print("黑色")

=======
Suggestion 3

def main():
    R,C = map(int,input().split())
    if R%2 == 0:
        if C%2 == 0:
            print('白色')
        else:
            print('黑色')
    else:
        if C%2 == 0:
            print('黑色')
        else:
            print('白色')

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 5

def print_color(r, c):
    if r % 2 == 0:
        if c % 2 == 0:
            print('白色')
        else:
            print('黑色')
    else:
        if c % 2 == 0:
            print('黑色')
        else:
            print('白色')

=======
Suggestion 6

def main():
    # 读取输入
    a = input()
    # 用空格分割
    b = a.split()
    # 转换成整数
    c = [int(i) for i in b]
    # print(c)
    # 读取行数
    R = c[0]
    # 读取列数
    C = c[1]
    # print(R)
    # print(C)
    # 判断
    if R % 2 == 0:
        if C % 2 == 0:
            print("黑色")
        else:
            print("白色")
    else:
        if C % 2 == 0:
            print("白色")
        else:
            print("黑色")

main()

=======
Suggestion 7

def main():
    # 读取输入
    line = input().split()
    # 转换为整数
    r = int(line[0])
    c = int(line[1])
    # 如果行列均为偶数，输出黑色
    if r % 2 == 0 and c % 2 == 0:
        print("black")
    # 如果行列均为奇数，输出黑色
    elif r % 2 == 1 and c % 2 == 1:
        print("black")
    # 否则输出白色
    else:
        print("white")

=======
Suggestion 8

def main():
    R,C = map(int,input().split())
    if R%2 == 0:
        if C%2 == 0:
            print("白色")
        else:
            print("黑色")
    else:
        if C%2 == 0:
            print("黑色")
        else:
            print("白色")
