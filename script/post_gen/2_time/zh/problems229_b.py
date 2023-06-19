Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    sum = A + B
    if sum >= 10**18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    if (A+B) < 10**10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a + b) < 10 ** 9:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 4

def easy_or_hard():
    A, B = map(int, input().split())
    if A + B >= 10 ** 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def sumAB(a, b):
    return a+b

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if a+b >= 10**10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a+b >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 8

def problem229_b():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a+b >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 9

def main():
    # 读取输入
    a, b = map(int, input().split())

    # 处理
    if a + b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 10

def main():
    A,B = map(int, input().split())
    if A+B >= 10**10:
        print("Hard")
    else:
        print("Easy")
