Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    line = input()
    a,b,c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    print(int(a*b/2))

=======
Suggestion 2

def main():
    # 读入数据
    a,b,c = map(int, input().split())
    # 计算面积
    s = a * b / 2
    # 输出结果
    print(int(s))

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())

    print(a*b//2)

=======
Suggestion 4

def problem116_a():
    a,b,c = map(int,input().split())
    print(int(a*b/2))

=======
Suggestion 5

def main():
    #定义变量
    AB = 0
    BC = 0
    CA = 0
    #输入变量
    AB,BC,CA = map(int,input().split())
    #计算面积
    area = int(AB * BC / 2)
    #输出结果
    print(area)

=======
Suggestion 6

def main():
    # input
    a,b,c = map(int, input().split())
    # output
    print(int(a*b/2))

=======
Suggestion 7

def triangle_area(a, b, c):
    return int((a * b) / 2)

=======
Suggestion 8

def main():
    # 读入数据
    line = input('请输入三角形的三边长，以空格分隔：')
    # 用空格分隔读入的数据
    line = line.split()
    # 把字符型数据转换成整数型数据
    line = [int(x) for x in line]
    # 计算三角形的面积
    area = line[0] * line[1] / 2
    # 打印结果
    print('三角形的面积是：', area)

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    print(int(a*b/2))
