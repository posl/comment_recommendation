Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 2

def swap(x,y):
    return y,x

x,y,z = map(int,input().split())
x,y = swap(x,y)
x,z = swap(x,z)
print(x,y,z)

=======
Suggestion 3

def exchange(a, b):
    return b, a

=======
Suggestion 4

def main():
    #输入
    x, y, z = map(int, input().split())
    #处理
    a = x
    b = y
    c = z
    x = c
    y = a
    z = b
    #输出
    print(x, y, z)

=======
Suggestion 5

def swap(a, b):
    return b, a
