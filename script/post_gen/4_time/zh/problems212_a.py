Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print("黄金")
    elif A == 0 and 0 < B:
        print("白银")
    else:
        print("合金")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == 0:
        print('Silver')
    elif b == 0:
        print('Gold')
    else:
        print('Alloy')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('黄金')
    elif a == 0 and b > 0:
        print('银')
    else:
        print('合金')

=======
Suggestion 4

def main():
    # 读取数据
    a, b = map(int, input().split())
    # 逻辑处理
    if a > 0 and b == 0:
        print('黄金')
    elif a == 0 and b > 0:
        print('银')
    else:
        print('合金')

=======
Suggestion 5

def problem212_a():
    A,B = map(int,input().split())
    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print("黄金")
    elif A==0 and B>0:
        print("银")
    else:
        print("合金")

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    if a > 0 and b == 0:
        print("黄金")
    elif a == 0 and b > 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print('黄金')
    elif A == 0 and 0 < B:
        print('银')
    else:
        print('合金')
