Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    x,y,z = map(int,input().split())
    if y > 0:
        print(-1)
        return
    print(-y+z)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if x > 0:
        print(-1)
    else:
        print((y - x) // (z + 1) + 1)

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > 0:
            print(-1)
        else:
            print(X - Y - Z)
    else:
        if Z < 0:
            print(-1)
        else:
            print(Y - X + Z)

=======
Suggestion 4

def main():
    x, y, z = map(int, input().split())
    if x < y:
        if y < z:
            print(-1)
        else:
            print(y-x)
    else:
        if z < y:
            print(-1)
        else:
            print(z-x)

=======
Suggestion 5

def main():
    X,Y,Z = map(int, input().split())
    if Y < Z:
        print(-1)
    else:
        print(int(X/(Y-Z)))

=======
Suggestion 6

def main():
    X, Y, Z = map(int, input().split())
    if Y > Z:
        print(-1)
    else:
        print(X // (Z - Y) - (X % (Z - Y) == 0))

=======
Suggestion 7

def main():
    x, y, z = map(int, input().split())
    if y > 0:
        print(-1)
    else:
        print(int((x-z)/(z-y)))

=======
Suggestion 8

def main():
    x,y,z = map(int,input().split())
    if x < y:
        if y < z:
            print(-1)
        else:
            print(abs(x-y)+z)
    else:
        print(x-y+z)

=======
Suggestion 9

def main():
    x, y, z = map(int, input().split())
    if y > x:
        print(-1)
    else:
        print(int((z * x) / (x - y) - 1))

=======
Suggestion 10

def main():
    x, y, z = map(int, input().split())
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        print(-1)
    else:
        print(abs(x - y) // z)
