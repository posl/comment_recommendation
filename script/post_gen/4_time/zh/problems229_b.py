Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a+b >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a + b >= 10**10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 3

def easy_or_hard(a,b):
    a = str(a)
    b = str(b)
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    for i in range(len(a)):
        if int(a[i]) + int(b[i]) > 9:
            return 'Hard'
    return 'Easy'

=======
Suggestion 4

def problem229_b():
    a, b = map(int, input().split())
    if a + b >= 10 ** 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def solve():
    a, b = map(int, input().split())
    if a + b >= 10 ** 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 6

def main():
    A,B = map(int, input().split())
    sum = A + B
    if sum < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 7

def main():
    A,B = map(int, input().split())
    if A+B < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 8

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算
    if (a + b) % 2 == 0:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if (a+b) < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 10

def problem229_b():
    A, B = map(int, input().split())
    if A + B >= 10**9:
        print("Hard")
    else:
        print("Easy")
