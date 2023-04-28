Synthesizing 10/10 solutions (Duplicates hidden)

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
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y <= 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    X,Y = map(int,input().split())
    if X < Y:
        if X+3 > Y:
            print("Yes")
        else:
            print("No")
    else:
        if Y+3 > X:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if abs(x - y) > 2:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    print('Yes' if x - y < 3 else 'No')

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if abs(x-y) >= 3:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    x,y = map(int, input().split())
    if x < y and y - x < 3:
        print("Yes")
    elif x > y and x - y < 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x,y = map(int,input().split())
    print("Yes" if (x+3) > y else "No")
