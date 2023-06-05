Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    import math

    for line in sys.stdin:
        a,b,c = map(int,line.split())
        s = (a+b+c)/2
        print(int(math.sqrt(s*(s-a)*(s-b)*(s-c))))

=======
Suggestion 2

def main():
    import sys
    import math
    line = sys.stdin.readline()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(int(area))

=======
Suggestion 3

def main():
    #读取输入数据
    a,b,c = map(int, input().split())
    #计算三角形面积
    s = a * b / 2
    #输出结果
    print(int(s))

=======
Suggestion 4

def get_area(a, b, c):
    return a * b / 2

=======
Suggestion 5

def main():
    edge = input()
    edge = edge.split()
    edge = list(map(int, edge))
    edge.sort()
    area = int(edge[0] * edge[1] / 2)
    print(area)

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    print(int(a*b/2))

=======
Suggestion 7

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

a, b, c = map(int, input().split())
print(int(triangle_area(a, b, c)))

=======
Suggestion 8

def main():
    # 从标准输入中读取
    # 读取的是字符串
    # 用空格分割字符串
    # 用map函数转换成整数
    # 用list函数转换成列表
    # 用tuple函数转换成元组
    # 用变量接收元组中的整数
    # 用算术表达式计算面积
    # 用print函数打印输出
    a, b, c = tuple(map(int, input().split()))
    print(int(a * b * 0.5))

=======
Suggestion 9

def main():
    abc = input()
    abc = abc.split()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    s = (a * b) / 2
    print(int(s))

=======
Suggestion 10

def main():
    # 读取输入
    s = input()
    # 用空格分割输入，得到字符串数组
    s = s.split()
    # 将字符串数组转换为整数数组
    s = [int(x) for x in s]
    # 计算面积
    area = s[0] * s[1] // 2
    # 输出结果
    print(area)
