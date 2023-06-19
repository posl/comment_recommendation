Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y = input().split('.')
    y = int(y)
    if y <= 2:
        print(x + '-')
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(x + '+')

=======
Suggestion 2

def main():
    x,y=map(float,input().split("."))
    if 0<=y<=2:
        print(int(x),end="-")
    elif 3<=y<=6:
        print(int(x),end="")
    else:
        print(int(x),end="+")

=======
Suggestion 3

def get_input():
    x, y = map(int, input().split('.'))
    return x, y

=======
Suggestion 4

def get_input():
    return input("请输入X.Y，其中Y是一个数字：")

=======
Suggestion 5

def print_x_y(x, y):
    if 0 <= y <= 2:
        print(str(x) + '-')
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x) + '+')

=======
Suggestion 6

def printXplusminus(X,Y):
    if 0 <= Y <= 2:
        print(str(X) + "-")
    elif 3 <= Y <= 6:
        print(str(X))
    elif 7 <= Y <= 9:
        print(str(X) + "+")

=======
Suggestion 7

def main():
    x, y = input().split(".")
    y = int(y)
    x = int(x)
    if 0 <= y <= 2:
        print(str(x) + "-")
    elif 3 <= y <= 6:
        print(str(x))
    else:
        print(str(x) + "+")

=======
Suggestion 8

def main():
    x,y = map(float, input().split('.'))
    if y <= 2:
        print('%d-'%x)
    elif y <= 6:
        print('%d'%x)
    else:
        print('%d+'%x)

=======
Suggestion 9

def printX(Y):
    if Y >= 0 and Y <= 2:
        print('X-')
    elif Y >= 3 and Y <= 6:
        print('X')
    elif Y >= 7 and Y <= 9:
        print('X+')

=======
Suggestion 10

def print_plus_minus(x, y):
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x + '+')
