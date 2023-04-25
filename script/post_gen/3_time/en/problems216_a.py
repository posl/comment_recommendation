Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(x)
    else:
        print(str(x) + "+")

=======
Suggestion 2

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print('{}-'.format(x))
    elif 3 <= y <= 6:
        print('{}'.format(x))
    elif 7 <= y <= 9:
        print('{}+'.format(x))

=======
Suggestion 3

def main():
    X, Y = input().split(".")
    Y = int(Y)
    if 0 <= Y <= 2:
        print(X + "-")
    elif 3 <= Y <= 6:
        print(X)
    else:
        print(X + "+")

=======
Suggestion 4

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(str(x) + "+")

=======
Suggestion 5

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
Suggestion 6

def main():
    X,Y = map(int,input().split("."))
    if Y <= 2:
        print("{}-".format(X))
    elif Y <= 6:
        print(X)
    else:
        print("{}+".format(X))

=======
Suggestion 7

def printSign(X, Y):
    if 0 <= Y and Y <= 2:
        print(str(X) + "-")
    elif 3 <= Y and Y <= 6:
        print(str(X))
    elif 7 <= Y and Y <= 9:
        print(str(X) + "+")

=======
Suggestion 8

def plusminus(x,y):
    if 0 <= y <= 2:
        print(str(x)+'-')
    elif 3 <= y <= 6:
        print(str(x))
    else:
        print(str(x)+'+')
