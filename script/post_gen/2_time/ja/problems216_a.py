Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if 0 <= int(y) <= 2:
        print(x, "-", sep="")
    elif 3 <= int(y) <= 6:
        print(x)
    else:
        print(x, "+", sep="")

=======
Suggestion 2

def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(x, "-", sep="")
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x, "+", sep="")

=======
Suggestion 3

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
Suggestion 4

def main():
    X, Y = map(int, input().split("."))
    if Y <= 2:
        print(X, "-", sep="")
    elif Y <= 6:
        print(X)
    else:
        print(X, "+", sep="")

main()

=======
Suggestion 5

def main():
    x = float(input())
    if x - int(x) < 0.3:
        print(int(x)-1)
    elif x - int(x) < 0.7:
        print(int(x))
    else:
        print(int(x)+1)

=======
Suggestion 6

def main():
    x = input()
    y = int(x[-1])
    if 0 <= y <= 2:
        print(x[:-2] + '-')
    elif 3 <= y <= 6:
        print(x[:-2])
    elif 7 <= y <= 9:
        print(x[:-2] + '+')

=======
Suggestion 7

def main():
    x, y = map(int, input().split("."))
    y = int(y)
    if y >= 0 and y <= 2:
        print(x - 1)
    elif y >= 3 and y <= 6:
        print(x)
    elif y >= 7 and y <= 9:
        print(x + 1)

=======
Suggestion 8

def main():
    x = input()
    x = x.split('.')
    if x[1] == '0':
        print(x[0] + '-')
    elif x[1] == '1' or x[1] == '2':
        print(x[0] + '-')
    elif x[1] == '3' or x[1] == '4' or x[1] == '5' or x[1] == '6':
        print(x[0])
    elif x[1] == '7' or x[1] == '8' or x[1] == '9':
        print(x[0] + '+')

=======
Suggestion 9

def main():
    x_y = input()
    x = x_y.split(".")[0]
    y = x_y.split(".")[1]
    if y <= "2":
        print(x + "-")
    elif y <= "6":
        print(x)
    else:
        print(x + "+")

=======
Suggestion 10

def main():
    x = input()
    if float(x) >= 0 and float(x) <= 2:
        print(int(float(x)), end = '-')
    elif float(x) >= 3 and float(x) <= 6:
        print(int(float(x)), end = '')
    elif float(x) >= 7 and float(x) <= 9:
        print(int(float(x)), end = '+')
