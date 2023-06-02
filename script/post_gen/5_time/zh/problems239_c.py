Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if (x1-x2)**2+(y1-y2)**2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5 and (x1 + x2) ** 2 + (y1 + y2) ** 2 == 10:
        print("Yes")
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 == 10 and (x1 + x2) ** 2 + (y1 + y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def f(x1,y1,x2,y2):
    if x1==x2 or y1==y2:
        return "No"
    if abs(x1-x2)==abs(y1-y2):
        return "Yes"
    else:
        return "No"

x1,y1,x2,y2=map(int,input().split())
print(f(x1,y1,x2,y2))

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 == 10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_square(n):
    return n == int(n ** 0.5) ** 2

x1, y1, x2, y2 = map(int, input().split())

=======
Suggestion 6

def problems239_c():
    pass

=======
Suggestion 7

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

x1, y1, x2, y2 = map(int, input().split())

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 == 5:
        print("Yes")
    elif ((x1 - y2)**2 + (y1 - x2)**2)**0.5 == 5:
        print("Yes")
    else:
        print("No")
