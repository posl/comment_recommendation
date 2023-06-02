Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(A / (A ** 2 + B ** 2) ** 0.5, B / (A ** 2 + B ** 2) ** 0.5)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    x = a/(a**2+b**2)**(1/2)
    y = b/(a**2+b**2)**(1/2)
    print(x,y)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    x = a/(a**2+b**2)**0.5
    y = b/(a**2+b**2)**0.5
    print(x,y)

=======
Suggestion 5

def problems246_b():
    import sys
    import math
    #sys.stdin = open("data/246_b.txt", "r")
    a, b = map(int, input().split())
    #print(a, b)
    #print(math.sqrt(a*a + b*b))
    x = a / math.sqrt(a*a + b*b)
    y = b / math.sqrt(a*a + b*b)
    print(x, y)


problems246_b()

=======
Suggestion 6

def solve(a,b):
    x = a / (a**2+b**2)**0.5
    y = b / (a**2+b**2)**0.5
    return x,y

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    x = A / (A ** 2 + B ** 2) ** 0.5
    y = B / (A ** 2 + B ** 2) ** 0.5
    print("{0:.12f} {1:.12f}".format(x, y))

=======
Suggestion 8

def get_distance(a, b):
    return (a**2 + b**2)**0.5

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    x = (A**2 - B**2)/(2*A)
    y = (A**2 - x**2)**0.5
    print(x, y)

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    x = 1
    y = 1
    if a != 0:
        x = (a**2 / (a**2 + b**2))**0.5
        y = (b**2 / (a**2 + b**2))**0.5
    print("{:.12f} {:.12f}".format(x, y))
