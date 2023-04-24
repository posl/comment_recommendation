Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return calc(n-1, x, y) + x + (n-2)*y

=======
Suggestion 2

def calc(N,X,Y):
    if N == 1:
        return 0
    elif N == 2:
        return X + Y
    else:
        return calc(N-1,X,Y) + X + calc(N-1,X,Y) + Y

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    print((N-1)*Y+X)

=======
Suggestion 4

def get_max_blue_jewels(N, X, Y):
    if N == 1:
        return 0

    if X == 1 and Y == 1:
        return (N - 1) * 2

    if X == 1:
        return (N - 1) * 2 * Y

    if Y == 1:
        return (N - 1) * 2 * X

    return (N - 1) * 2 * X * Y

=======
Suggestion 5

def main():
    n, x, y = map(int, input().split())
    print(n, x, y)
    return 0

=======
Suggestion 6

def main():
    n, x, y = map(int, input().split())
    print((n-1) * x + y)

=======
Suggestion 7

def get_input():
    return map(int, raw_input().split())

=======
Suggestion 8

def get_input():
    return map(int, input().split())

=======
Suggestion 9

def convert_red(n, x):
    return n-1, x+n

=======
Suggestion 10

def solve():
    return 0
