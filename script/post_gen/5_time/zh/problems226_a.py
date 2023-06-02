Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = float(input())
    x = int(X)
    y = X - x
    if y < 0.25:
        print(x)
    elif y < 0.75:
        print(x+0.5)
    else:
        print(x+1)

=======
Suggestion 2

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 3

def main():
    x = float(input())
    x *= 1000
    x = int(x + 0.5)
    print(x // 1000)

=======
Suggestion 4

def main():
    X = float(input())
    print(round(X))

=======
Suggestion 5

def main():
    x = float(input())
    x = x + 0.5
    x = int(x)
    print(x)

=======
Suggestion 6

def round_up(x):
    if x < 0.25:
        return 0
    elif 0.25 <= x < 0.75:
        return 0.5
    else:
        return 1
