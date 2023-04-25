Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if ((x_1 - x_2)**2 + (y_1 - y_2)**2)**(1/2) == ((x_1)**2 + (y_1)**2)**(1/2) + ((x_2)**2 + (y_2)**2)**(1/2):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5 and (x1 - y1) * (x2 - y2) != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5 and (x1 - y1) ** 2 + (x2 - y2) ** 2 == 5 and (x1 - y2) ** 2 + (x2 - y1) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    print('Yes' if (x1-x2)**2 + (y1-y2)**2 == 5 else 'No')

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1-x2)**2 + (y1-y2)**2)**0.5 == ((x1-0)**2 + (y1-0)**2)**0.5 == ((x2-0)**2 + (y2-0)**2)**0.5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    if x1 == x2 or y1 == y2:
        print("Yes")
        return
    if abs(x1 - x2) == abs(y1 - y2):
        print("Yes")
        return
    print("No")

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1-x2)**2 + (y1-y2)**2)**(1/2) == ((x1-x2)**2 + (y1-y2)**2)**(1/2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if ((x1-x2)**2+(y1-y2)**2)**0.5 == ((x1-0)**2+(y1-0)**2)**0.5 + ((x2-0)**2+(y2-0)**2)**0.5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2)**2 + (y1 - y2)**2 == (x1 - y1)**2 or (x1 - x2)**2 + (y1 - y2)**2 == (x1 + y1)**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def is_lattice_point(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return False
    else:
        return True
