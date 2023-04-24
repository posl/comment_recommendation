Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if 0 <= int(y) <= 2:
        print(x, "-", sep="")
    elif 3 <= int(y) <= 6:
        print(x)
    elif 7 <= int(y) <= 9:
        print(x, "+", sep="")

=======
Suggestion 2

def main():
    x = input().split('.')
    if 0 <= int(x[1]) <= 2:
        print(x[0] + '-')
    elif 3 <= int(x[1]) <= 6:
        print(x[0])
    else:
        print(x[0] + '+')

=======
Suggestion 3

def main():
    x, y = input().split('.')
    if 0 <= int(y) <= 2:
        print(x+'-')
    elif 3 <= int(y) <= 6:
        print(x)
    elif 7 <= int(y) <= 9:
        print(x+'+')

=======
Suggestion 4

def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(x, "-", sep="")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x, "+", sep="")

=======
Suggestion 5

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(x, "-", sep="")
    elif y <= 6:
        print(x)
    else:
        print(x, "+", sep="")

=======
Suggestion 6

def main():
    x = input()
    if x[-1] == '0' or x[-1] == '1' or x[-1] == '2':
        print(x[:-2] + '-')
    elif x[-1] == '3' or x[-1] == '4' or x[-1] == '5' or x[-1] == '6':
        print(x[:-2])
    else:
        print(x[:-2] + '+')

main()

=======
Suggestion 7

def main():
    x, y = map(int, input().split('.'))

    if 0 <= int(y) <= 2:
        print(x, '-', sep='')
    elif 3 <= int(y) <= 6:
        print(x)
    elif 7 <= int(y) <= 9:
        print(x, '+', sep='')

=======
Suggestion 8

def main():
    X, Y = input().split(".")
    Y = int(Y[0])
    if Y <= 2:
        print(X + "-")
    elif Y <= 6:
        print(X)
    else:
        print(X + "+")

main()

=======
Suggestion 9

def main():
    x = float(input())
    if x - int(x) >= 0.0 and x - int(x) <= 0.2:
        print(int(x) - 1)
    elif x - int(x) >= 0.3 and x - int(x) <= 0.6:
        print(int(x))
    elif x - int(x) >= 0.7 and x - int(x) <= 0.9:
        print(int(x) + 1)
