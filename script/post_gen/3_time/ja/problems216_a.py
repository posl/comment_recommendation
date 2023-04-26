Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split("."))
    if 0 <= Y <= 2:
        print(X, "-", sep="")
    elif 3 <= Y <= 6:
        print(X)
    else:
        print(X, "+", sep="")

=======
Suggestion 2

def main():
    x, y = input().split(".")
    x = int(x)
    y = int(y)
    if 0 <= y <= 2:
        print(x - 1)
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + 1)

=======
Suggestion 3

def main():
    x = input()
    if x[-1] == '0' or x[-1] == '1' or x[-1] == '2':
        print(x[:-2] + '-')
    elif x[-1] == '3' or x[-1] == '4' or x[-1] == '5' or x[-1] == '6':
        print(x[:-2])
    else:
        print(x[:-2] + '+')

=======
Suggestion 4

def main():
    X, Y = input().split(".")
    if Y in ["0", "1", "2"]:
        print(X + "-")
    elif Y in ["3", "4", "5", "6"]:
        print(X)
    else:
        print(X + "+")

=======
Suggestion 5

def main():
    x = input()
    if x[-1] == "0" or x[-1] == "1" or x[-1] == "2":
        print(x[:-2] + "-")
    elif x[-1] == "3" or x[-1] == "4" or x[-1] == "5" or x[-1] == "6":
        print(x[:-2])
    elif x[-1] == "7" or x[-1] == "8" or x[-1] == "9":
        print(x[:-2] + "+")

=======
Suggestion 6

def main():
    X = input()
    if X[2] == '0' or X[2] == '1' or X[2] == '2':
        print(X[0:2] + '-')
    elif X[2] == '3' or X[2] == '4' or X[2] == '5' or X[2] == '6':
        print(X[0:2])
    elif X[2] == '7' or X[2] == '8' or X[2] == '9':
        print(X[0:2] + '+')

=======
Suggestion 7

def main():
    x = input()
    if x[2] == '0' or x[2] == '1' or x[2] == '2':
        print(x[0:2]+'-')
    elif x[2] == '3' or x[2] == '4' or x[2] == '5' or x[2] == '6':
        print(x[0:2])
    elif x[2] == '7' or x[2] == '8' or x[2] == '9':
        print(x[0:2]+'+')

=======
Suggestion 8

def main():
    x, y = map(int, input().split("."))
    if y < 3:
        print(x, "-", sep="")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x, "+", sep="")

=======
Suggestion 9

def main():
    x = int(input())
    y = int(input())
    if y < 3:
        print(x - 1)
    elif y < 7:
        print(x)
    else:
        print(x + 1)

=======
Suggestion 10

def main():
    x = input()
    if x[2] in ['0','1','2']:
        print(int(x[0])-1)
    elif x[2] in ['3','4','5','6']:
        print(int(x[0]))
    else:
        print(int(x[0])+1)
