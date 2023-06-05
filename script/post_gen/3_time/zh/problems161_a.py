Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    print(c,a,b)

=======
Suggestion 3

def main():
    # 读取输入
    x, y, z = map(int, input().split())

    # 交换
    tmp = x
    x = y
    y = tmp

    # 交换
    tmp = x
    x = z
    z = tmp

    # 打印
    print(x, y, z)

=======
Suggestion 4

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)
