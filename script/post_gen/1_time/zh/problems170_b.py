Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        j = X - i
        if 2*i + 4*j == Y:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def check(a, b):
    for i in range(a+1):
        for j in range(a+1):
            if i * 2 + j * 4 == b:
                return True
    return False

a, b = map(int, input().split())

=======
Suggestion 3

def cal(X,Y):
    if (Y-2*X)%2 == 0:
        A = (Y-2*X)/2
        B = X-A
        if A >= 0 and B >= 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def solve(x, y):
    for i in range(x + 1):
        if i * 2 + (x - i) * 4 == y:
            return True
    return False

x, y = map(int, input().split())

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x == y == 2:
        print('Yes')
    elif x * 2 <= y <= x * 4 and y % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def check(x,y):
    for i in range(x+1):
        for j in range(x+1-i):
            if 2*i+4*j == y:
                return True
    return False

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    if y%2 == 0:
        if x <= y/2 and x >= y/4:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

main()

=======
Suggestion 8

def solve():
    x, y = map(int, input().split())
    for i in range(x + 1):
        if i * 2 + (x - i) * 4 == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def solve():
    x,y = map(int,input().split())
    for i in range(x+1):
        j = x - i
        if 2*i + 4*j == y:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 10

def main():
    X, Y = map(int, input().split())
    if X == 1 and Y == 2:
        print("Yes")
    elif X == 2 and Y == 4:
        print("Yes")
    elif X == 3 and Y == 6:
        print("Yes")
    elif X == 4 and Y == 8:
        print("Yes")
    elif X == 5 and Y == 10:
        print("Yes")
    elif X == 6 and Y == 12:
        print("Yes")
    elif X == 7 and Y == 14:
        print("Yes")
    elif X == 8 and Y == 16:
        print("Yes")
    elif X == 9 and Y == 18:
        print("Yes")
    elif X == 10 and Y == 20:
        print("Yes")
    elif X == 11 and Y == 22:
        print("Yes")
    elif X == 12 and Y == 24:
        print("Yes")
    elif X == 13 and Y == 26:
        print("Yes")
    elif X == 14 and Y == 28:
        print("Yes")
    elif X == 15 and Y == 30:
        print("Yes")
    elif X == 16 and Y == 32:
        print("Yes")
    elif X == 17 and Y == 34:
        print("Yes")
    elif X == 18 and Y == 36:
        print("Yes")
    elif X == 19 and Y == 38:
        print("Yes")
    elif X == 20 and Y == 40:
        print("Yes")
    elif X == 21 and Y == 42:
        print("Yes")
    elif X == 22 and Y == 44:
        print("Yes")
    elif X == 23 and Y == 46:
        print("Yes")
    elif X == 24 and Y == 48:
        print("Yes")
    elif X == 25 and Y == 50:
        print("Yes")
    elif X == 26 and Y == 52:
        print("Yes")
    elif X == 27 and Y == 54:
        print("Yes")
    elif X == 28 and Y == 56:
        print("Yes")
    elif X == 29 and Y ==
