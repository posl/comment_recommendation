Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    # 通过判断a+b的和来确定正确答案
    if a + b == 4:
        print(1)
    elif a + b == 3:
        print(2)
    else:
        print(3)

=======
Suggestion 2

def get_correct_answer(a,b):
    if a == 1 and b == 2:
        return 3
    elif a == 1 and b == 3:
        return 2
    elif a == 2 and b == 1:
        return 3
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return 2
    elif a == 3 and b == 2:
        return 1

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    print(6 - A - B)

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    if a == 1 and b == 2:
        print(3)
    elif a == 1 and b == 3:
        print(2)
    elif a == 2 and b == 1:
        print(3)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 1:
        print(2)
    elif a == 3 and b == 2:
        print(1)
    else:
        print("输入错误")

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    print(6 - a - b)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    if a == 1 and b == 2:
        print(3)
    elif a == 2 and b == 1:
        print(3)
    elif a == 1 and b == 3:
        print(2)
    elif a == 3 and b == 1:
        print(2)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 2:
        print(1)

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())
    if a == 1 and b == 2:
        print(3)
    elif a == 2 and b == 1:
        print(3)
    elif a == 3 and b == 1:
        print(2)
    elif a == 1 and b == 3:
        print(2)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 2:
        print(1)

=======
Suggestion 8

def printCorrectAnswer(A, B):
    print(6 - A - B)

=======
Suggestion 9

def main():
    a = int(input())
    b = int(input())
    if a == 1:
        if b == 2:
            print(3)
        else:
            print(2)
    elif a == 2:
        if b == 1:
            print(3)
        else:
            print(1)
    else:
        if b == 1:
            print(2)
        else:
            print(1)
