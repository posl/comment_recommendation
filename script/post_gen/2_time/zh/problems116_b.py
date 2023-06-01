Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    line = input()
    # 分割输入，得到三条边的长度
    values = line.split()
    # 将三条边的长度转换为整数
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    # 计算面积
    area = a * b // 2
    # 输出面积
    print(area)

=======
Suggestion 2

def main():
    # 读取输入
    a,b,c = map(int,input().split())
    # 计算面积
    s = (a*b)/2
    # 打印输出
    print(int(s))

=======
Suggestion 3

def main():
    # 读取输入
    sides = input().split()
    # 计算面积
    area = (int(sides[0]) * int(sides[1])) / 2
    # 打印输出
    print(int(area))

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    print(int(a*b/2))
    return

=======
Suggestion 5

def triangle_area(a, b, c):
    return a * b / 2

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    print(int(a*b/2))

=======
Suggestion 7

def main():
    #input
    a,b,c = map(int, input().split())
    #compute
    area = a*b/2
    #output
    print(int(area))

=======
Suggestion 8

def main():
    import math
    a,b,c = map(int, input().split())
    s = (a * b) / 2
    print(int(s))

=======
Suggestion 9

def main():
    import sys
    line = sys.stdin.readline()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    s = (a * b) / 2
    print(int(s))

=======
Suggestion 10

def main():
    a,b,c = map(int,input().split())
    print(int((a*b)/2))
