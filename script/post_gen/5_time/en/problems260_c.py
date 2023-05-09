Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, x, y):
    if x > y:
        return 0
    elif x == y:
        return (n - 1) * x
    else:
        return (n - 1) * x + y

=======
Suggestion 2

def red_jewel_to_blue_jewel(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x + y
    else:
        return red_jewel_to_blue_jewel(n-1, x, y) + x + red_jewel_to_blue_jewel(n-1, x, y) + y

=======
Suggestion 3

def calc(N, X, Y):
    if N == 1:
        return 0
    else:
        return (N - 1) * X + Y

=======
Suggestion 4

def main():
    import sys
    import math
    input = sys.stdin.readline
    n, x, y = map(int, input().split())
    if x > y:
        print((n-1)*y)
    else:
        if n == 1:
            print(0)
        else:
            print((n-2)*x+y)

=======
Suggestion 5

def main():
    n, x, y = map(int, input().split())
    print(0)

=======
Suggestion 6

def problem():
    n, x, y = map(int, input().split())
    return (n-1)*y + x

print(problem())

=======
Suggestion 7

def get_jewel_count(N, X, Y):
    if X > Y:
        return 0
    else:
        return (N-1)*X + Y

=======
Suggestion 8

def main():
    pass
