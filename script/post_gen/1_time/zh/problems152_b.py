Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

=======
Suggestion 2

def main():
    # 读取输入
    input_line = input()
    a, b = map(int, input_line.split())

    # 求解并输出
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 3

def problem152_b(a,b):
    a = int(a)
    b = int(b)
    a_str = str(a)
    b_str = str(b)
    a_str = a_str * b
    b_str = b_str * a
    if a_str < b_str:
        print(a_str)
    else:
        print(b_str)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    a_str = str(a)
    b_str = str(b)
    if a_str == b_str:
        print(a_str*a)
    elif a_str < b_str:
        print(a_str*b)
    else:
        print(b_str*a)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a>b:
        print(str(b)*a)
    elif a<b:
        print(str(a)*b)
    else:
        print(str(a)*b)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a > b :
        print(str(b)*a)
    else:
        print(str(a)*b)

=======
Suggestion 7

def main():
    a,b = [int(i) for i in input().split()]
    if a > b:
        print(str(b)*a)
    else:
        print(str(a)*b)

=======
Suggestion 8

def main():
    a = input("请输入a：")
    b = input("请输入b：")
    if a<b:
        print(a*a)
    elif a>b:
        print(b*b)
    else:
        print(a*a)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a == b:
        print(str(a)*b)
    elif a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 10

def main():
    # 读取输入
    a, b = input().split()
    # 计算
    a = int(a)
    b = int(b)
    a_str = str(a)
    b_str = str(b)
    a_str *= b
    b_str *= a
    if a_str < b_str:
        print(a_str)
    else:
        print(b_str)
    return
