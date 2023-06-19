Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solution():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("白银")
    else:
        print("合金")


solution()

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a > 0 and b == 0:
        print("黄金")
    elif a == 0 and b > 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 3

def main():
    # 读取输入
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("合金")
    elif a > 0 and b == 0:
        print("黄金")
    elif a == 0 and b > 0:
        print("银")
    else:
        print("输入错误")

=======
Suggestion 4

def problem212_a():
    a,b = map(int,input().split())
    if a > 0 and b == 0:
        print("黄金")
    elif a == 0 and b > 0:
        print("白银")
    else:
        print("合金")

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print('黄金')
    elif A==0 and B>0:
        print('银')
    else:
        print('合金')

=======
Suggestion 6

def problem():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('黄金')
    elif a == 0 and b > 0:
        print('银')
    else:
        print('合金')

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a == 0:
        print('银')
    elif b == 0:
        print('黄金')
    else:
        print('合金')

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a == 0 and b != 0:
        print("银")
    elif a != 0 and b == 0:
        print("黄金")
    elif a != 0 and b != 0:
        print("合金")

=======
Suggestion 9

def main():
    A, B = map(int, input().split())

    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("银")
    else:
        print("合金")
