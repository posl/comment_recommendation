Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    a,b = map(int,input().split())
    print(2**a+2**b)

=======
Suggestion 2

def main():
    input = raw_input()
    input = input.split()
    a = int(input[0])
    b = int(input[1])
    if a == 0 and b == 0:
        print 0
    elif a == 0:
        print b
    elif b == 0:
        print a
    else:
        print 7 - a - b

=======
Suggestion 3

def main():
    while True:
        try:
            a,b = map(int,input().split())
            if a == 0 and b == 0:
                print(0)
            elif a == 1 and b == 1:
                print(4)
            elif a == 2 and b == 2:
                print(3)
            elif a == 3 and b == 3:
                print(2)
            elif a == 4 and b == 4:
                print(1)
            elif a == 0 and b == 1:
                print(3)
            elif a == 1 and b == 0:
                print(3)
            elif a == 0 and b == 2:
                print(2)
            elif a == 2 and b == 0:
                print(2)
            elif a == 0 and b == 3:
                print(1)
            elif a == 3 and b == 0:
                print(1)
            elif a == 1 and b == 2:
                print(1)
            elif a == 2 and b == 1:
                print(1)
            elif a == 1 and b == 3:
                print(0)
            elif a == 3 and b == 1:
                print(0)
            elif a == 2 and b == 3:
                print(0)
            elif a == 3 and b == 2:
                print(0)
        except:
            break

=======
Suggestion 4

def main():
    # 1. 输入数据
    s = input()
    a, b = map(int, s.split())

    # 2. 计算并输出
    print(7 - a - b)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(7-a+7-b)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(7 - a - b)

=======
Suggestion 7

def solve():
    A, B = map(int, input().split())
    print(7 - A - B)

=======
Suggestion 8

def solve(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 1 and b == 1:
        return 4
    elif a == 1 and b == 2:
        return 3
    elif a == 1 and b == 3:
        return 2
    elif a == 1 and b == 4:
        return 1
    elif a == 2 and b == 1:
        return 3
    elif a == 2 and b == 2:
        return 2
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return 2
    elif a == 3 and b == 2:
        return 1
    elif a == 4 and b == 1:
        return 1
    else:
        return 0

=======
Suggestion 9

def solve():
    A, B = map(int, input().split())
    print(3 - A - B)
