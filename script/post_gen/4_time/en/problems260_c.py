Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    input_line = input().split()
    n = int(input_line[0])
    x = int(input_line[1])
    y = int(input_line[2])

    if n == 1:
        print(0)
    else:
        print((n-1)*x+y)

=======
Suggestion 2

def main():
    a = input()
    a = a.split()
    n = int(a[0])
    x = int(a[1])
    y = int(a[2])
    if n == 1:
        print(0)
    else:
        print((n-1)*x+y)

=======
Suggestion 3

def main():
    n, x, y = map(int, input().split())
    print((n - 1) * x + y)

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    print(N, X, Y)

=======
Suggestion 5

def getBlueJewels(n, x, y):
    if n == 1:
        return 0
    elif x >= y:
        return getBlueJewels(n-1, x, y) + x
    else:
        return max(getBlueJewels(n-1, x, y) + x, getBlueJewels(n-1, x, y) + y)

=======
Suggestion 6

def get_input():
    n, x, y = map(int, input().split())
    return n, x, y

=======
Suggestion 7

def main():
    n, x, y = map(int, input().split())
    print(n, x, y)

=======
Suggestion 8

def calc(N, X, Y):
    if N == 1:
        return 0
    else:
        return (N-1)*X + (N-1)*(N-2)*Y//2

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    print(2**N * (X+Y))

=======
Suggestion 10

def get_blue_jewel_count(n, x, y):
    if y >= x:
        return 0
    else:
        return (n-1) * (y + (n-2) * (x-y))
