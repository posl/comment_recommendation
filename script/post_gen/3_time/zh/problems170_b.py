Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print('Yes')
    elif x * 2 <= y <= x * 4 and y % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and y >= 2 * x and y <= 4 * x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def check(x, y):
    for i in range(x + 1):
        if 2 * i + 4 * (x - i) == y:
            return True
    return False

x, y = map(int, input().split())

=======
Suggestion 4

def check(x,y):
    if y%2 == 0 and 2*x <= y and y <= 4*x:
        return True
    else:
        return False

=======
Suggestion 5

def func(x,y):
    if 2*x <= y and y <= 4*x:
        return "Yes"
    else:
        return "No"

x,y = map(int,input().split())
print(func(x,y))

=======
Suggestion 6

def check(X, Y):
    for i in range(0, X+1):
        for j in range(0, X+1):
            if i + j == X and i*2 + j*4 == Y:
                return True
    return False

X, Y = map(int, input().split())

=======
Suggestion 7

def solve(x, y):
    for i in range(x + 1):
        if (i * 2 + (x - i) * 4) == y:
            return True
    return False

x, y = map(int, input().split())

=======
Suggestion 8

def check(x, y):
    if x == 1:
        if y == 2:
            return True
        else:
            return False
    elif x == 2:
        if y == 4 or y == 2:
            return True
        else:
            return False
    else:
        return False

=======
Suggestion 9

def solve():
    x, y = map(int, input().split())
    if 2 * x <= y and y <= 4 * x and y % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def solution():
    x, y = map(int, input().split())
    for i in range(x + 1):
        if 2 * i + 4 * (x - i) == y:
            print('Yes')
            return
    print('No')

solution()
