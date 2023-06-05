Synthesizing 10/10 solutions

=======
Suggestion 1

def solution(x, y):
    if 0 <= y <= 2:
        return x + "-"
    elif 3 <= y <= 6:
        return x
    else:
        return x + "+"

=======
Suggestion 2

def main():
    # 读取输入
    x, y = map(float, input().split('.'))
    if 0 <= y <= 2:
        print(int(x), end='-')
    elif 3 <= y <= 6:
        print(int(x), end='')
    else:
        print(int(x), end='+')

=======
Suggestion 3

def main():
    x, y = map(float, input().split('.'))
    if y <= 2:
        print(int(x), end='')
        print('-')
    elif y <= 6:
        print(int(x), end='')
    else:
        print(int(x), end='')
        print('+')

=======
Suggestion 4

def printX_Y(X, Y):
    if 0 <= Y <= 2:
        print("{}-".format(X))
    elif 3 <= Y <= 6:
        print("{}".format(X))
    elif 7 <= Y <= 9:
        print("{}+".format(X))

=======
Suggestion 5

def check(x,y):
    if y>=0 and y<=2:
        return "X-"
    elif y>=3 and y<=6:
        return "X"
    elif y>=7 and y<=9:
        return "X+"

=======
Suggestion 6

def main():
    x, y = map(float, input().split("."))
    if y <= 2:
        print(str(int(x)) + "-")
    elif y <= 6:
        print(int(x))
    else:
        print(str(int(x)) + "+")

=======
Suggestion 7

def main():
    x, y = map(float, input().split("."))
    if 0 <= y <= 2:
        print(int(x) - 1, end="")
        print("-")
    elif 3 <= y <= 6:
        print(int(x), end="")
        print("")
    elif 7 <= y <= 9:
        print(int(x) + 1, end="")
        print("+")

=======
Suggestion 8

def main():
    x,y = map(float,input().split('.'))
    if y <= 2:
        print(int(x),end='-')
    elif y <= 6:
        print(int(x))
    else:
        print(int(x),end='+')

=======
Suggestion 9

def main():
    x,y = map(float,input().split("."))
    if 0 <= y <= 2:
        print(int(x) - 1,end="")
        print("-")
    elif 3 <= y <= 6:
        print(int(x),end="")
    elif 7 <= y <= 9:
        print(int(x) + 1,end="")
        print("+")
main()

=======
Suggestion 10

def main():
    input_str = input()
    x, y = input_str.split('.')
    y = int(y)
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + '+')
