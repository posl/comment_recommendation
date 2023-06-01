Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a, b):
    return b, a

=======
Suggestion 2

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return (a,b)

=======
Suggestion 3

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

=======
Suggestion 4

def main():
    A = input("A: ")
    B = input("B: ")
    C = input("C: ")
    print(C, A, B)

=======
Suggestion 5

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 6

def main():
    # 读取输入
    x,y,z = map(int, input().split())
    # 交换
    a = x
    x = y
    y = a
    # 交换
    b = x
    x = z
    z = b
    # 输出
    print(x,y,z)

=======
Suggestion 7

def main():
    # 读取输入
    x, y, z = map(int, input().split())

    # 交换
    x, y = y, x
    x, z = z, x

    # 打印
    print(x, y, z)

=======
Suggestion 8

def swap(x, y, z):
    return z, x, y
