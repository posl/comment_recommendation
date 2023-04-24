Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print("Yes")
        else:
            print("No")
    else:
        if y + 3 > x:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if X < Y:
        if X + 3 > Y:
            print("Yes")
        else:
            print("No")
    else:
        if Y + 3 > X:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x < y:
        if y - x < 3:
            print("Yes")
        else:
            print("No")
    else:
        if x - y < 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x < y:
        if (y - x) < 3:
            print("Yes")
        else:
            print("No")
    else:
        if (x - y) < 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x < y:
        if y - x >= 3:
            print("No")
        else:
            print("Yes")
    else:
        if x - y >= 3:
            print("No")
        else:
            print("Yes")

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if X - Y < 3:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    x, y = map(int, input().split())

    if x < y:
        if y - x >= 3:
            print("Yes")
        else:
            print("No")
    else:
        if x - y >= 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    if (y - x) >= 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    X, Y = map(int, input().split())
    if abs(X - Y) > 2:
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    if X < Y:
        if (Y - X) < 3:
            print("Yes")
        else:
            print("No")
    else:
        if (X - Y) < 3:
            print("Yes")
        else:
            print("No")
