Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(str(x)+"-")
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x)+"+")

=======
Suggestion 2

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(str(x))
    else:
        print(str(x) + "+")

=======
Suggestion 3

def main():
    x,y = input().split('.')
    y = int(y)
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + '+')

=======
Suggestion 4

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(x, '-')
    elif y <= 6:
        print(x)
    else:
        print(x, '+')

=======
Suggestion 5

def main():
    x, y = input().split('.')
    y = int(y)
    if y <= 2:
        print(x + '-')
    elif y <= 6:
        print(x)
    else:
        print(x + '+')

=======
Suggestion 6

def main():
    l = input().split(".")
    x = int(l[0])
    y = int(l[1])
    if 0 <= y <= 2:
        print(str(x) + "-")
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x) + "+")

=======
Suggestion 7

def main():
    x,y = map(float,input().split("."))
    if y <= 2:
        print(str(int(x))+"-")
    elif y <= 6:
        print(int(x))
    else:
        print(str(int(x))+"+")

=======
Suggestion 8

def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(str(x)+"-")
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(str(x)+"+")

=======
Suggestion 9

def main():
    x,y = map(int,input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(str(x) + "+")

=======
Suggestion 10

def main():
    X, Y = input().rstrip().split(".")
    Y = int(Y)

    if 0 <= Y <= 2:
        print(X + "-")
    elif 3 <= Y <= 6:
        print(X)
    else:
        print(X + "+")
