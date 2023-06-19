Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #input
    a,b,c = map(int,input().split())
    #calc
    s = int(0.5*a*b)
    #output
    print(s)

=======
Suggestion 2

def main():
    # 读入
    ab, bc, ca = map(int, input().split())
    # 计算
    print(int(ab * bc / 2))

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    s = a*b/2
    print(int(s))

=======
Suggestion 4

def getArea(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

a,b,c = map(int, input().split())
print(int(getArea(a,b,c)))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(int(a * b * 0.5))

=======
Suggestion 6

def area(a,b,c):
    return a*b/2
a,b,c = map(int,input().split())
print(int(area(a,b,c)))

=======
Suggestion 7

def main():
    # 读入数据
    # 由于输入数据是一行，所以使用input()函数
    # input()函数会读入一行数据，并将末尾的换行符去掉
    # 然后，将这行数据赋值给变量line
    line = input()
    # 使用空格分割line
    # 分割后，line是一个列表，列表中的每个元素都是字符串
    # 使用map()函数，将列表中的每个元素转换为整数
    a, b, c = map(int, line.split())
    # 计算三角形面积
    s = a * b / 2
    # 打印结果
    print(int(s))

main()

=======
Suggestion 8

def main():
    import math
    a,b,c = map(int,input().split())
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(int(area))

=======
Suggestion 9

def main():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    print(int(a*b/2))

=======
Suggestion 10

def main():
    # 读取输入
    abc = input().split()
    # 转换为整数
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    # 计算面积
    s = a * b / 2
    # 输出结果
    print(int(s))
