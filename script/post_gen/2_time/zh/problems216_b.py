Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y = map(float,input().split("."))
    if 0 <= y <= 2:
        print(int(x) - 1,end="")
        print("-")
    elif 3 <= y <= 6:
        print(int(x))
    else:
        print(int(x) + 1,end="")
        print("+")

=======
Suggestion 2

def main():
    x,y = map(float, input().split("."))
    if 0 <= y <= 2:
        print(int(x), end="")
        print("-")
    elif 3 <= y <= 6:
        print(int(x), end="")
    else:
        print(int(x), end="")
        print("+")

=======
Suggestion 3

def problem216_a():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(x, '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x, '+')

=======
Suggestion 4

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
Suggestion 5

def main():
    x,y=input().split(".")
    y=int(y)
    x=int(x)
    if 0<=y<=2:
        print(x,end="")
        print("-")
    elif 3<=y<=6:
        print(x,end="")
    elif 7<=y<=9:
        print(x,end="")
        print("+")

=======
Suggestion 6

def print_sign(num):
    if num <= 2:
        print('X-')
    elif num <= 6:
        print('X')
    else:
        print('X+')

=======
Suggestion 7

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(str(x) + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(str(x) + '+')

=======
Suggestion 8

def main():
    x,y = input().split(".")
    y = int(y)
    if y <= 2:
        print(x+"-")
    elif y <= 6:
        print(x)
    else:
        print(x+"+")

main()

=======
Suggestion 9

def print_result(x, y):
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x + '+')

=======
Suggestion 10

def main():
    x,y = map(float,input().split('.'))
    if 0<=y<=2:
        print(str(int(x))+'-')
    elif 3<=y<=6:
        print(str(int(x)))
    else:
        print(str(int(x))+'+')
