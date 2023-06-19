Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    A, B, C = map(int, input().split())
    if A == B:
        print('=')
    elif C % 2 == 0:
        if abs(A) == abs(B):
            print('=')
        elif abs(A) > abs(B):
            print('>')
        else:
            print('<')
    else:
        if A > B:
            print('>')
        else:
            print('<')

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if pow(a,c) < pow(b,c):
        print("<")
    elif pow(a,c) > pow(b,c):
        print(">")
    else:
        print("=")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("=")
    elif c % 2 == 0:
        if abs(a) == abs(b):
            print("=")
        elif abs(a) > abs(b):
            print(">")
        else:
            print("<")
    elif c % 2 == 1:
        if a > b:
            print(">")
        else:
            print("<")

=======
Suggestion 4

def pow(a, b):
    if b == 0:
        return 1
    else:
        return a * pow(a, b - 1)

=======
Suggestion 5

def pow(a,b):
    return a**b

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print('=')
        return
    if c % 2 == 0:
        if abs(a) == abs(b):
            print('=')
            return
        else:
            if abs(a) > abs(b):
                print('>')
            else:
                print('<')
            return
    else:
        if a > b:
            print('>')
        else:
            print('<')
        return

=======
Suggestion 7

def main():
    # 读取输入
    line = input()
    # 将输入按空格分割成列表
    line = line.split()
    # 将输入的每个元素转换为整数
    line = [int(x) for x in line]
    # 将输入的每个元素分别赋值给A、B、C
    A, B, C = line[0], line[1], line[2]
    # 计算pow(A,C)和pow(B,C)，并比较大小
    if pow(A, C) > pow(B, C):
        print('>')
    elif pow(A, C) < pow(B, C):
        print('<')
    else:
        print('=')

=======
Suggestion 8

def pow(a,b):
    if a > 0:
        return a**b
    elif a < 0:
        if b%2 == 0:
            return abs(a**b)
        else:
            return -abs(a**b)
    else:
        return 0

=======
Suggestion 9

def comparePow(a, b, c):
    if pow(a, c) > pow(b, c):
        return ">"
    elif pow(a, c) < pow(b, c):
        return "<"
    else:
        return "="

print(comparePow(3, 2, 4))
print(comparePow(-7, 7, 2))
print(comparePow(-8, 6, 3))
