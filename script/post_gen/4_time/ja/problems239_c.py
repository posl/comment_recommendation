Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
        return
    if (x1 + y1) == (x2 + y2):
        print('Yes')
        return
    if (x1 - y1) == (x2 - y2):
        print('Yes')
        return
    print('No')

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 == 5:
        print('Yes')
        return
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 == 50:
        print('Yes')
        return
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 == 25:
        print('Yes')
        return
    print('No')

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    if x1 == x2:
        if abs(y1 - y2) == (5)**(1/2):
            print("Yes")
            return
    if y1 == y2:
        if abs(x1 - x2) == (5)**(1/2):
            print("Yes")
            return
    if abs(x1 - x2) == (5)**(1/2) and abs(y1 - y2) == (5)**(1/2):
        print("Yes")
        return
    print("No")
    return

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x_1,y_1,x_2,y_2 = map(int,input().split())
    if x_1 == x_2 and y_1 == y_2:
        print("No")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 10:
        print("Yes")
        return
    if x_1 == x_2:
        if abs(y_1 - y_2) == 5:
            print("Yes")
            return
        if abs(y_1 - y_2) == 10:
            print("Yes")
            return
    if y_1 == y_2:
        if abs(x_1 - x_2) == 5:
            print("Yes")
            return
        if abs(x_1 - x_2) == 10:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        print("No")
    else:
        if abs(x1 - x2) == abs(y1 - y2):
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def problems239_c():
    x1,y1,x2,y2 = map(int,input().split())
    if (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2) == (5)**(1/2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def is_integer(n):
    return n % 1 == 0
