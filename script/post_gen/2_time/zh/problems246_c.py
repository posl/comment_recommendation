Synthesizing 10/10 solutions

=======
Suggestion 1

def move(x,y):
    x = x - 0.5
    y = y - 0.5
    return x,y

=======
Suggestion 2

def getPoint(A,B):
    # x = A / (A + B)
    # y = B / (A + B)
    x = 1 / (1 + B / A)
    y = 1 / (1 + A / B)
    return x,y

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        print(0,0)
    else:
        x = A/(A**2 + B**2)**0.5
        y = B/(A**2 + B**2)**0.5
        print(x,y)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print(a/b, b/a)

=======
Suggestion 5

def get_pos(a, b):
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    else:
        c = (a**2 + b**2)**0.5
        return a/c, b/c

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    print(A/(A**2+B**2)**0.5,B/(A**2+B**2)**0.5)

=======
Suggestion 7

def get_distance(a, b):
    return (a*a + b*b)**0.5

=======
Suggestion 8

def problems246_b():
    a,b = [int(i) for i in input().split()]
    x = a * 1.0 / (a * a + b * b) ** 0.5
    y = b * 1.0 / (a * a + b * b) ** 0.5
    print(x,y)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    print(a/(a**2+b**2)**0.5,b/(a**2+b**2)**0.5)

=======
Suggestion 10

def main():
    a,b = map(int, input().split())
    x = a/(a**2+b**2)**0.5
    y = b/(a**2+b**2)**0.5
    print('{:.12f} {:.12f}'.format(x,y))
