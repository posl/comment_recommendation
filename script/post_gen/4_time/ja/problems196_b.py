Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = input()
    X = X.split(".")
    print(X[0])

=======
Suggestion 2

def main():
    x = input()
    if '.' in x:
        print(x[0:x.find('.')])
    else:
        print(x)
main()

=======
Suggestion 3

def main():
    X = input()
    if '.' in X:
        X = X.split('.')[0]
    print(X)
    return

=======
Suggestion 4

def main():
    # -*- coding: utf-8 -*-
    import sys
    import math

    # input
    X = input()

    # solve
    print(math.floor(float(X)))

=======
Suggestion 5

def main():
    x = input()
    print(x.split(".")[0])

=======
Suggestion 6

def main():
    x = input()
    print(int(float(x)))

=======
Suggestion 7

def main():
    x = input()
    print(int(float(x)))

main()

=======
Suggestion 8

def main():
    x = input()
    print(int(x.split('.')[0]))

=======
Suggestion 9

def main():
    print(int(input()))
