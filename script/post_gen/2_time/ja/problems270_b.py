Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if z > 0:
        if x > y:
            print(x - y)
        else:
            print(-1)
    else:
        if x < y:
            print(y - x)
        else:
            print(-1)

=======
Suggestion 2

def main():
    X, Y, Z = map(int, input().split())
    if abs(X) > abs(Y):
        print(abs(X) + abs(X - Z))
    else:
        print(abs(X) + abs(Y) + abs(Y - Z))

=======
Suggestion 3

def main():
    x, y, z = map(int, input().split())
    if z >= 0:
        print(abs(x-y))
    else:
        print(-1)

=======
Suggestion 4

def main():
    x, y, z = map(int, input().split())
    if x > 0:
        print(x - y)
    elif x < 0:
        print(-x + y)
    else:
        if y > 0:
            print(y - z)
        elif y < 0:
            print(-y + z)
        else:
            print(z)

=======
Suggestion 5

def main():
    X, Y, Z = map(int, input().split())
    if Z >= X:
        print(-1)
    else:
        print(abs(X-Y))

=======
Suggestion 6

def main():
    x,y,z = map(int,input().split())
    if y < 0:
        print(abs(x) + abs(y) + abs(z))
    else:
        print(-1)

=======
Suggestion 7

def main():
    x,y,z = map(int,input().split())
    if x > y:
        if -z < y:
            print(-1)
        else:
            print(x-y)
    else:
        if -z < x:
            print(-1)
        else:
            print(y-x)

=======
Suggestion 8

def main():
    X,Y,Z = map(int,input().split())
    if X > 0:
        if Y < 0:
            if Z > 0:
                print(abs(X-Y)+abs(Z-Y))
            else:
                print(abs(X-Y))
        else:
            if Z > 0:
                print(abs(X-Y)+abs(Z-Y))
            else:
                print(-1)
    else:
        if Y < 0:
            if Z > 0:
                print(-1)
            else:
                print(abs(X-Y))
        else:
            if Z > 0:
                print(abs(X-Y)+abs(Z-Y))
            else:
                print(abs(X-Y))

=======
Suggestion 9

def main():
    X,Y,Z = map(int,input().split())
    if Z < Y:
        print(-1)
    else:
        print(X/(Z-Y))

=======
Suggestion 10

def main():
    x,y,z=map(int,input().split())
    if z>y:
        print(-1)
    else:
        print(x+y-z)
