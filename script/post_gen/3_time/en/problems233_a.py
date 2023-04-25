Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(y - x)

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        print(Y-X)

=======
Suggestion 3

def main():
    x,y = map(int, input().split())
    z = y - x
    if z % 10 == 0:
        print(z // 10)
    else:
        print(z // 10 + 1)

=======
Suggestion 4

def main():
    x, y = list(map(int, input().split()))
    if x >= y:
        print(0)
    else:
        print(y - x)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print((y - x) if (y - x) > 0 else 0)

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print(0 if x >= y else y - x)

=======
Suggestion 7

def problem233_a():
    x, y = map(int, input().split())
    if x < y:
        print(y - x)
    else:
        print(0)

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    print(max(0, y - x))

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    print(y // x)
