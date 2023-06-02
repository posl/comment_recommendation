Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a, b):
    return b, a

=======
Suggestion 2

def main():
    # 读取输入
    x, y, z = map(int, input().split())
    # 交换
    x, y = y, x
    x, z = z, x
    # 输出
    print(x, y, z)

=======
Suggestion 3

def main():
    x,y,z = map(int,input().split())
    print(z,x,y)

=======
Suggestion 4

def swap(a,b):
    a,b = b,a
    return a,b

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(c,a,b)

=======
Suggestion 6

def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    print(a[0], a[1], a[2])

=======
Suggestion 7

def swap(x,y):
    return y,x

a,b,c = map(int,input().split())
a,b = swap(a,b)
a,c = swap(a,c)
print(a,b,c)
