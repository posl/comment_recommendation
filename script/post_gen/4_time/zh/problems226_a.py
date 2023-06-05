Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = float(input())
    x = x + 0.001
    print(int(x))

=======
Suggestion 2

def round(x):
    if x - int(x) < 0.5:
        return int(x)
    else:
        return int(x) + 1

=======
Suggestion 3

def main():
    x = float(input())
    x = x + 0.0001
    print(int(x))

=======
Suggestion 4

def main():
    import sys
    import math

    for line in sys.stdin:
        x = float(line)
        print(int(math.floor(x + 0.5)))

=======
Suggestion 5

def main():
    # input
    x = float(input())
    # process
    y = int(round(x))
    # output
    print(y)

=======
Suggestion 6

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

=======
Suggestion 7

def get_input():
    x = float(input())
    return x

=======
Suggestion 8

def main():
    a = float(input())
    b = int(a * 10 + 0.5)
    print(b // 10)

=======
Suggestion 9

def main():
    X = float(input())
    print(round(X))
