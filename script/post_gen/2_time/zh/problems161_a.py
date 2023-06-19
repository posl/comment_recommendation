Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y,z = map(int,input().split())
    print(z,x,y)
    
main()

=======
Suggestion 2

def exchange(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

=======
Suggestion 3

def main():
    x,y,z = map(int,input().split())
    print(z,x,y)

=======
Suggestion 4

def main():
    # 从标准输入读取整数
    # 用map函数将输入的整数分成三个变量
    x, y, z = map(int, input().split())
    # 输出三个变量
    print(z, x, y)

=======
Suggestion 5

def main():
    X,Y,Z = map(int, input().split())
    print(Z,X,Y)

=======
Suggestion 6

def swap(l):
    l[0], l[1] = l[1], l[0]

=======
Suggestion 7

def main():
    # 读取输入
    x, y, z = map(int, input().split())
    # 输出
    print(z, x, y)

=======
Suggestion 8

def exchange(x, y, z):
    return y, z, x
