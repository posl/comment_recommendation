Synthesizing 10/10 solutions

=======
Suggestion 1

def check(X, Y):
    if X > Y:
        if X - Y < 3:
            return True
        else:
            return False
    else:
        if Y - X < 3:
            return True
        else:
            return False

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y < 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

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
Suggestion 4

def main():
    x, y = map(int, input().split())
    if (x + 3) > y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x < y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X > Y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    if x < y:
        x,y = y,x
    if x - y <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x,y = map(int, input().split())
    if x > y:
        if y + 3 > x:
            print('Yes')
        else:
            print('No')
    else:
        if x + 3 > y:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    x,y = map(int, input().split())
    if x > y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    x, y = map(int, input().split())
    print("Yes" if x + 3 > y else "No")
