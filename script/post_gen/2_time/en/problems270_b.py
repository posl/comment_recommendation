Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        if Z < Y:
            print(abs(X-Z))
        else:
            print(abs(X-Y)+abs(Z-Y))
    else:
        print(-1)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if y < z:
        print(-1)
    else:
        print(abs(x))

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())

    if X > 0:
        if Y > 0:
            if Z > 0:
                if X > Y:
                    if X > Z:
                        if Y > Z:
                            print(X - Y + X - Z)
                        else:
                            print(X - Y + Z - Y)
                    else:
                        print(X - Y + Z - X)
                else:
                    if X > Z:
                        print(Y - X + X - Z)
                    else:
                        print(Y - X + Z - X)
            else:
                if X > Y:
                    print(X - Y + X - Z)
                else:
                    print(Y - X + X - Z)
        else:
            if Z > 0:
                if X > Z:
                    print(X - Y + X - Z)
                else:
                    print(X - Y + Z - X)
            else:
                print(X - Y + X - Z)
    else:
        if Y > 0:
            if Z > 0:
                if X > Y:
                    print(X - Y + X - Z)
                else:
                    print(Y - X + X - Z)
            else:
                print(X - Y + X - Z)
        else:
            if Z > 0:
                if X > Y:
                    print(X - Y + X - Z)
                else:
                    print(Y - X + X - Z)
            else:
                print(X - Y + X - Z)

=======
Suggestion 4

def main():
    x,y,z = map(int, input().split())
    if x < y:
        if z < y:
            print(abs(x-z))
        else:
            print(abs(x-y)+abs(z-y))
    else:
        if z > y:
            print(abs(x-z))
        else:
            print(abs(x-y)+abs(z-y))

=======
Suggestion 5

def main():
    x,y,z = map(int,input().split())
    if x > 0:
        if z < y:
            print(x - y)
        else:
            print(-1)
    else:
        if z < y:
            print(y - x)
        else:
            print(-1)

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(-1)
    else:
        print(abs(x-z) + abs(z-y))

=======
Suggestion 7

def main():
    x, y, z = map(int, input().split())
    if x < y:
        if z > y:
            print(-1)
        else:
            print(x-y)
    else:
        if z > x:
            print(-1)
        else:
            print(y-x)

=======
Suggestion 8

def main():
    # Read input
    X, Y, Z = map(int, input().split())

    # Check if Takahashi can reach the goal
    if abs(X) < abs(Z):
        print(-1)
        return

    # Check if the wall is between the origin and the goal
    if abs(Z) < abs(Y) < abs(X):
        print(abs(X) - abs(Y))
    else:
        print(abs(X))

=======
Suggestion 9

def main():
    x,y,z = map(int, input().split())
    if x < y < z:
        print(z - x)
    else:
        print(-1)

=======
Suggestion 10

def get_input():
    return list(map(int, input().split()))
