Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(2)
    elif x == 0 and y == 2:
        print(1)
    elif x == 1 and y == 0:
        print(1)
    elif x == 1 and y == 2:
        print(2)
    elif x == 2 and y == 0:
        print(2)
    elif x == 2 and y == 1:
        print(1)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3-(x+y))

=======
Suggestion 4

def solve(x, y):
    if (x == y):
        return x
    else:
        return 3 - (x + y)

=======
Suggestion 5

def solve(x,y):
    if x == y:
        return x
    else:
        return 3-x-y

=======
Suggestion 6

def get_input():
    x,y = input().split()
    return x,y
