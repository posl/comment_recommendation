Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print("{0}-".format(x))
    elif 3 <= y <= 6:
        print("{0}".format(x))
    else:
        print("{0}+".format(x))

=======
Suggestion 2

def main():
    x,y = input().split(".")
    y = int(y)
    if y <= 2:
        print(x+"-")
    elif y <= 6:
        print(x)
    else:
        print(x+"+")

=======
Suggestion 3

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(str(x) + '-')
    elif y <= 6:
        print(x)
    else:
        print(str(x) + '+')

=======
Suggestion 4

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
Suggestion 5

def main():
    x,y = input().split(".")
    y = int(y)
    if 0 <= y and y <= 2:
        print(x+"-")
    elif 3 <= y and y <= 6:
        print(x)
    elif 7 <= y and y <= 9:
        print(x+"+")

=======
Suggestion 6

def main():
    x, y = map(str, input().split("."))
    y = int(y)
    if 0 <= y <= 2:
        print(x + "-")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + "+")

=======
Suggestion 7

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(str(x)+'-')
    elif 3 <= y <= 6:
        print(str(x))
    else:
        print(str(x)+'+')

=======
Suggestion 8

def main():
    X, Y = input().split('.')
    Y = int(Y)
    if Y <= 2:
        print(X + '-')
    elif Y <= 6:
        print(X)
    else:
        print(X + '+')

=======
Suggestion 9

def main():
    # input
    X,Y = input().split(".")
    X = int(X)
    Y = int(Y)

    # compute

    # output
    if 0 <= Y and Y <= 2:
        print(str(X) + "-")
    elif 3 <= Y and Y <= 6:
        print(X)
    else:
        print(str(X) + "+")

=======
Suggestion 10

def main():
    x = float(input())
    y = int(x*10)%10

    if y <= 2:
        print(str(int(x))+'-')
    elif y <= 6:
        print(int(x))
    else:
        print(str(int(x))+'+')
