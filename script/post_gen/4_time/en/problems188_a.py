Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y < 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x < y:
        if y - x < 3:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x < y and (y - x) <= 2:
        print("Yes")
    elif x > y and (x - y) <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print('Yes')
            return
    else:
        if y + 3 > x:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if (x + 3) > y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if abs(x-y) <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    print("Yes" if x < y and x + 3 > y else "No")

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    print("Yes" if x + 3 > y else "No")

=======
Suggestion 9

def main():
    x,y = map(int, input().split())
    if (x-y) < 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    #input
    X, Y = map(int, input().split())

    #check if the team behind can turn the tables with a successful three-point goal
    if X < Y:
        if X + 3 > Y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
