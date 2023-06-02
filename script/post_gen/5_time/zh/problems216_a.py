Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def judge(x,y):
    if y<=2:
        print(str(x)+'-')
    elif 3<=y<=6:
        print(str(x))
    elif 7<=y<=9:
        print(str(x)+'+')

=======
Suggestion 2

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print('{}-'.format(x))
    elif 3 <= y <= 6:
        print(x)
    else:
        print('{}+'.format(x))

=======
Suggestion 3

def main():
    x,y = input().split('.')
    y = int(y)
    if y <= 2:
        print(x + '-')
    elif y <= 6:
        print(x)
    else:
        print(x + '+')

=======
Suggestion 4

def main():
    x,y = map(float,input().split("."))
    if y<=2:
        print(int(x),end="-")
    elif y<=6:
        print(int(x))
    else:
        print(int(x),end="+")

=======
Suggestion 5

def print_grade(x, y):
    if y <= 2:
        print(x + "-")
    elif y <= 6:
        print(x)
    else:
        print(x + "+")

=======
Suggestion 6

def main():
    x,y = map(float,input().split("."))
    if 0 <= y <= 2:
        print(int(x) , end="")
        print("-")
    elif 3 <= y <= 6:
        print(int(x))
    elif 7 <= y <= 9:
        print(int(x) , end="")
        print("+")

=======
Suggestion 7

def main():
    x, y = map(float, input().split("."))
    if 0 <= y <= 2:
        print(int(x), end="-")
    elif 3 <= y <= 6:
        print(int(x), end="")
    elif 7 <= y <= 9:
        print(int(x), end="+")
    else:
        print("error")

=======
Suggestion 8

def print_sign(x,y):
    if 0 <= y <= 2:
        print(str(x) + '-')
    elif 3 <= y <= 6:
        print(str(x))
    else:
        print(str(x) + '+')
