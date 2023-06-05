Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 2

def main():
    a = input("请输入第一个数：")
    b = input("请输入第二个数：")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if a >= 1 and a <= 20 and b >= 1 and b <= 20:
            print(a * b)
        else:
            print("输入的数不在范围内")
    else:
        print("输入的不是整数")

=======
Suggestion 3

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算结果
    if a < 1 or a > 20 or b < 1 or b > 20:
        print(-1)
    else:
        print(a * b)

=======
Suggestion 4

def main():
    # 读取输入
    a, b = map(int, input().split())

    # 计算
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if 1<=a<=20 and 1<=b<=20:
        print(a*b)
    else:
        print(-1)
