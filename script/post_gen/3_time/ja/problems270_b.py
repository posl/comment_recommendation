Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(z - y + z - x)
    elif x > y > z:
        print(x - y + x - z)
    elif x < y > z:
        print(abs(x - z) + abs(y - z))
    else:
        print(-1)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if x < y:
        print(-1)
    else:
        print(x - y + z)

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())
    if X < Y < Z:
        print(Z - X)
    else:
        print(-1)

=======
Suggestion 4

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        print(X - Y)
    else:
        print(-1)

=======
Suggestion 5

def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        if X < Z:
            print(Z - X)
        else:
            print(-1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if abs(x) < abs(y):
        if abs(x) < abs(z):
            print(abs(z - x))
        else:
            print(abs(x - z))
    else:
        if abs(y) < abs(z):
            print(abs(z - y))
        else:
            print(abs(y - z))

=======
Suggestion 7

def main():
    #入力
    X, Y, Z = map(int, input().split())
    #出力
    if X < Y < Z:
        print(-1)
    elif X > Y > Z:
        print(-1)
    else:
        print(abs(X - Y) + abs(Y - Z))

=======
Suggestion 8

def main():
    #入力
    X, Y, Z = map(int, input().split())

    #処理
    if abs(X) < abs(Y):
        if abs(X) < abs(Z):
            print(abs(X) + abs(Z))
        else:
            print(abs(X) + abs(Y))
    else:
        if abs(Y) < abs(Z):
            print(abs(Y) + abs(Z))
        else:
            print(abs(X) + abs(Y))

=======
Suggestion 9

def main():
    x,y,z = map(int,input().split())
    if z > 0:
        if y > 0:
            if x > 0:
                if x < y:
                    print(y - x)
                else:
                    print(-1)
            else:
                print(y - x)
        else:
            if x > 0:
                print(y - x)
            else:
                if x > y:
                    print(y - x)
                else:
                    print(-1)
    else:
        print(-1)

=======
Suggestion 10

def main():
    X,Y,Z = map(int,input().split())
    if X>0 and Y<0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)-abs(Z))
        else:
            print(abs(X)+abs(Y)+abs(Z))
    elif X<0 and Y>0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)+abs(Z))
        else:
            print(abs(X)+abs(Y)-abs(Z))
    elif X<0 and Y<0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)+abs(Z))
        else:
            print(abs(X)+abs(Y)+abs(Z))
    elif X>0 and Y>0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)-abs(Z))
        else:
            print(abs(X)+abs(Y)-abs(Z))
    else:
        print(-1)
