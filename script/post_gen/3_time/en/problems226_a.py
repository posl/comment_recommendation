Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = float(input())
    if x % 1 >= 0.5:
        print(int(x) + 1)
    else:
        print(int(x))

=======
Suggestion 2

def main():
    X = float(input())
    if X % 1 >= 0.5:
        print(int(X) + 1)
    else:
        print(int(X))

=======
Suggestion 3

def main():
    x = float(input())
    if x - int(x) < 0.5:
        print(int(x))
    else:
        print(int(x)+1)

=======
Suggestion 4

def main():
    X = input()
    if int(X[-1]) < 5:
        print(int(X[0]))
    else:
        print(int(X[0]) + 1)

=======
Suggestion 5

def main():
    x = float(input())
    if x < 0:
        print(int(x-0.5))
    else:
        print(int(x+0.5))

=======
Suggestion 6

def main():
    x = float(input())
    print(int(x+0.5))

=======
Suggestion 7

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 8

def roundUp(x):
    if x%1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

=======
Suggestion 9

def main():
    x = float(input())
    print(int(round(x)))

=======
Suggestion 10

def main():
    print(round(float(input())))
