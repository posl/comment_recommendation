Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0 and Y >= 2 * X and Y <= 4 * X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if (y % 2 == 0) and (y >= 2 * x) and (y <= 4 * x):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and 2*x <= y <= 4*x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if (x*2 <= y) and (x*4 >= y) and (y%2 == 0):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
    X, Y = map(int, input().split())
    if Y % 2 == 0 and 2 * X <= Y and Y <= 4 * X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X*2 <= Y <= X*4 and Y%2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    if y%2 == 0 and 2*x <= y <= 4*x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x,y = map(int,input().split())
    if (y % 2 == 0) and (2 * x <= y) and (4 * x >= y):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    if x == 2:
        if y == 2 or y == 4:
            print('Yes')
        else:
            print('No')
    elif x == 4:
        if y == 2 or y == 4 or y == 6 or y == 8:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 10

def problem():
    x,y = map(int, input().split())
    if y % 2 == 0 and 2 * x <= y and y <= 4 * x:
        print("Yes")
    else:
        print("No")

problem()
