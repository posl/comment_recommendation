Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem216a():
    x,y = input().split('.')
    y = int(y)
    if y <= 2:
        print(x+'-')
    elif y <= 6:
        print(x)
    else:
        print(x+'+')

=======
Suggestion 2

def print_x_y(x, y):
    if 0 <= y <= 2:
        print(str(x) + '-')
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x) + '+')

=======
Suggestion 3

def print_sign_of_x(x):
    if 0 <= x <= 2:
        print(str(x) + "-")
    elif 3 <= x <= 6:
        print(str(x))
    elif 7 <= x <= 9:
        print(str(x) + "+")
    else:
        print("error")

=======
Suggestion 4

def main():
    x,y = map(float, input().split('.'))
    if y >= 0 and y <= 2:
        print(int(x)+'-')
    elif y >= 3 and y <= 6:
        print(int(x))
    elif y >= 7 and y <= 9:
        print(int(x)+'+')

=======
Suggestion 5

def print_result(x, y):
    if 0 <= y <= 2:
        print(str(x) + "-")
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x) + "+")

=======
Suggestion 6

def main():
    x, y = input().split('.')
    y = int(y)
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + '+')

=======
Suggestion 7

def main():
    x,y=input().split('.')
    y=int(y)
    if y>=0 and y<=2:
        print(x+'-')
    elif y>=3 and y<=6:
        print(x)
    elif y>=7 and y<=9:
        print(x+'+')

=======
Suggestion 8

def f(x,y):
    if 0 <= y <= 2:
        print(str(x)+'-')
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x)+'+')

=======
Suggestion 9

def print_x_y(x,y):
    if 0 <= y and y <= 2:
        print(x + "-")
    elif 3 <= y and y <= 6:
        print(x)
    elif 7 <= y and y <= 9:
        print(x + "+")
