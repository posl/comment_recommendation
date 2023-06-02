Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    import math
    # 获取输入
    input_line = sys.stdin.readline()
    # 分割输入
    input_line = input_line.split()
    # 转化为整数
    input_line = [int(i) for i in input_line]
    # 计算
    area = input_line[0] * input_line[1] / 2
    # 输出
    print(int(area))

=======
Suggestion 2

def area(a, b, c):
    return a * b / 2

=======
Suggestion 3

def tri_area(a, b, c):
    return a * b / 2

=======
Suggestion 4

def main():
    # 读入三角形的三条边
    a, b, c = map(int, input().split())
    # 计算三角形的面积
    s = (a * b) // 2
    # 打印输出
    print(s)

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(int(a*b/2))

=======
Suggestion 6

def cal_area(a,b):
    return a*b/2

=======
Suggestion 7

def area_of_triangle(a,b,c):
    return a*b/2

=======
Suggestion 8

def main():
    print("请输入三角形三边的长度：")
    a,b,c=map(int,input().split())
    s=(a*b)/2
    print("三角形的面积是：",s)
main()

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    s = (a * b) / 2
    print(int(s))

=======
Suggestion 10

def area_triangle(a,b,c):
    return (a*b)/2
