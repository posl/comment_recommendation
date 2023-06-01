Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A != 0 and B == 0:
        print("黄金")
    elif A == 0 and B != 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 2

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 处理
    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A == 0:
        print("银")
    elif B == 0:
        print("黄金")
    else:
        print("合金")

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a > 0 and b == 0:
        print("黄金")
    elif a == 0 and b > 0:
        print("银")
    else:
        print("合金")

main()

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('黄金')
    elif a == 0 and b > 0:
        print('银')
    else:
        print('合金')

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if a != 0 and b == 0:
        print("黄金")
    elif a == 0 and b != 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print("黄金")
    elif A==0 and B>0:
        print("银")
    else:
        print("合金")
main()

=======
Suggestion 8

def main():
    x,y = map(int,input().split())
    if x>0 and y>0:
        print('合金')
    elif x==0 and y>0:
        print('银')
    elif x>0 and y==0:
        print('黄金')

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a == 0:
        print('银')
    elif b == 0:
        print('黄金')
    else:
        print('合金')
