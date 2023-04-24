Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if y < 0:
        print(abs(x) + abs(y) + abs(z))
    else:
        print(-1)

=======
Suggestion 2

def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if X < Z:
        X, Z = Z, X
    if X < Y + Z:
        print(X - Y - Z)
    else:
        print(-1)

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        print(-1)
    else:
        print(X - Z)

=======
Suggestion 4

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > Y:
            print(abs(X-Z))
        else:
            print(-1)
    else:
        if Z > X:
            print(abs(Y-Z))
        else:
            print(-1)

=======
Suggestion 5

def main():
    X, Y, Z = map(int, input().split())
    if X < Y and Z < Y:
        print(Y - X)
    elif X < Y and Y < Z:
        print(Z - X)
    elif Y < X and Z < X:
        print(X - Y)
    else:
        print(-1)

=======
Suggestion 6

def main():
    # 入力
    X, Y, Z = map(int, input().split())

    # 出力
    if X < Y < Z or Z < Y < X:
        print(abs(X - Y) + abs(Y - Z))
    else:
        print(-1)

=======
Suggestion 7

def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        print(Y - X)
    else:
        print(-1)

=======
Suggestion 8

def main():
    X,Y,Z = map(int,input().split())
    if Z < 0:
        print(-1)
    elif abs(X) < abs(Y):
        print(-1)
    else:
        print(abs(X))

=======
Suggestion 9

def main():
    x,y,z = map(int,input().split())
    if x<z:
        print(-1)
    elif x<z+y:
        print(z+y-x)
    else:
        print(0)

=======
Suggestion 10

def main():
    #入力
    X,Y,Z = map(int,input().split())

    #出力
    if X<Z and Z<Y:
        print(Y-X)
    elif X>Z and Z>Y:
        print(X-Y)
    else:
        print(-1)
