Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if z >= y:
        print(-1)
    else:
        print(x // (y - z) * (y - z) + x % (y - z))

=======
Suggestion 2

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > Y:
            print(X - Y)
        else:
            print(-1)
    else:
        if Z > Y:
            print(-1)
        else:
            print(X - Z)

=======
Suggestion 3

def main():
    X,Y,Z = map(int,input().split())
    if X > Y:
        if Z < Y:
            print(-1)
        else:
            print(X-Z)
    else:
        if Z > Y:
            print(-1)
        else:
            print(Z+X)

=======
Suggestion 4

def main():
    X, Y, Z = [int(x) for x in input().split()]
    if X > 0:
        print(X - Y)
    elif X < 0:
        print(-X + Y)
    else:
        if Z > 0:
            print(Y - Z)
        else:
            print(-Y - Z)

=======
Suggestion 5

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(-1)
    else:
        print(abs(x-z))

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if x < y:
        if x < z < y:
            print(y - x)
        else:
            print(-1)
    elif x > y:
        if y < z < x:
            print(x - y)
        else:
            print(-1)
    else:
        print(-1)

=======
Suggestion 7

def main():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(-1)
    elif x < z < y:
        print(-1)
    else:
        print(abs(x - z))

=======
Suggestion 8

def main():
    x,y,z = map(int,input().split())
    if z > y:
        print(x-z)
    else:
        print(-1)

=======
Suggestion 9

def main():
    x, y, z = map(int, input().split())
    if x < y and x > z:
        print(y - z)
    else:
        print(-1)

=======
Suggestion 10

def main():
    X,Y,Z = map(int,input().split())
    if X<0 and Y>0:
        if Z<Y:
            print(abs(X)+abs(Z)+abs(Y))
        else:
            print(-1)
    else:
        print(abs(X)-abs(Z))
