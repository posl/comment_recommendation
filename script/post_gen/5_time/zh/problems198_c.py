Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    R,X,Y = map(int, input().split())
    if (X**2+Y**2)**(1/2) == R:
        print(1)
    elif (X**2+Y**2)**(1/2) < R:
        print(2)
    else:
        if (X**2+Y**2)**(1/2) % R == 0:
            print(int((X**2+Y**2)**(1/2)/R))
        else:
            print(int((X**2+Y**2)**(1/2)/R)+1)

=======
Suggestion 3

def main():
    R,X,Y = map(int,input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print((X**2 + Y**2)**0.5//R + 1)

=======
Suggestion 4

def solve():
    import sys
    import math
    R,X,Y = map(int, sys.stdin.readline().split())
    distance = math.sqrt(X**2 + Y**2)
    if distance % R == 0:
        print(int(distance/R))
    else:
        print(int(distance/R)+1)

=======
Suggestion 5

def main():
    R, X, Y = map(int, input().split())
    if X*X+Y*Y < R*R:
        print(2)
    else:
        print((X*X+Y*Y+R*R-1)//(R*R))

=======
Suggestion 6

def main():
    # input
    R, X, Y = map(int, input().split())

    # compute

    # output
    print( (X**2+Y**2)**(1/2)//R if (X**2+Y**2)**(1/2)%R == 0 else (X**2+Y**2)**(1/2)//R+1 )

=======
Suggestion 7

def main():
    R, X, Y = map(int, input().split())
    if (X ** 2 + Y ** 2) ** (1 / 2) % R == 0:
        print(int((X ** 2 + Y ** 2) ** (1 / 2) / R))
    else:
        print(int((X ** 2 + Y ** 2) ** (1 / 2) // R + 1))

=======
Suggestion 8

def problems198_c():
    pass

=======
Suggestion 9

def main():
    R, X, Y = map(int, input().split())
    if R*R > X*X + Y*Y:
        print(2)
    else:
        print((X*X + Y*Y + R*R - 1)//(R*R))
