Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 2

def main():
    x1,y1,x2,y2=map(int,input().split())
    if ((x1-x2)**2+(y1-y2)**2)**(1/2)==(5)**(1/2):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
    elif (x_1 - x_2) ** 2 + (y_1 - y_2 + 1) ** 2 == 5:
        print("Yes")
    elif (x_1 - x_2) ** 2 + (y_1 - y_2 - 1) ** 2 == 5:
        print("Yes")
    elif (x_1 - x_2 + 1) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
    elif (x_1 - x_2 - 1) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 5

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    elif (x1-x2)**2 + (y1-y2)**2 == 5:
        print("Yes")
        return
    elif (x1-x2)**2 + (y1-y2)**2 == 50:
        print("Yes")
        return
    else:
        print("No")
        return

=======
Suggestion 6

def problems239_c(x_1, y_1, x_2, y_2):
    if x_1 == x_2 and y_1 == y_2:
        return "No"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 10:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 50:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 90:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 130:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 170:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 210:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 250:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 290:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 330:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 370:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 410:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 450:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 490:
        return "Yes"
    if (x_1 - x_2)**2 + (y_1 - y_2)**2 == 530:
        return "Yes"
    if (x_1 - x_2

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        if abs(x1 - x2) + abs(y1 - y2) <= 6:
            print('Yes')
            return
    print('No')
