Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(x - y - z)
    else:
        print(-1)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(x - y + z)
    else:
        print(-1)

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > 0:
            print(-1)
        else:
            print(X - Y + abs(Z))
    else:
        print(-1)

=======
Suggestion 4

def main():
    x, y, z = map(int, input().split())
    a = x - z
    b = x + z
    if y < a or b < y:
        print(-1)
    else:
        print(a)

=======
Suggestion 5

def main():
    x, y, z = map(int, input().split())

    if x > 0 and y > 0 and z > 0:
        if x > y:
            print(x - y + z)
        else:
            print(z - y + x)
    elif x > 0 and y < 0 and z < 0:
        if x > -y:
            print(x - -y + -z)
        else:
            print(-z - -y + x)
    elif x < 0 and y < 0 and z < 0:
        if -x > -y:
            print(-x - -y + -z)
        else:
            print(-z - -y + -x)
    elif x < 0 and y > 0 and z > 0:
        if -x > y:
            print(-x - y + z)
        else:
            print(z - y + -x)
    elif x > 0 and y > 0 and z < 0:
        if x > y:
            print(x - y + -z)
        else:
            print(-z - y + x)
    elif x > 0 and y < 0 and z > 0:
        if x > -y:
            print(x - -y + z)
        else:
            print(z - -y + x)
    elif x < 0 and y < 0 and z > 0:
        if -x > -y:
            print(-x - -y + z)
        else:
            print(z - -y + -x)
    elif x < 0 and y > 0 and z < 0:
        if -x > y:
            print(-x - y + -z)
        else:
            print(-z - y + -x)
    else:
        print(-1)

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if y < x:
        print(-1)
    else:
        print(z + (y - x) // 2)

=======
Suggestion 7

def main():
    # input
    x, y, z = map(int, input().split())

    # compute
    ans = 0
    if x < y:
        ans += y - x
    else:
        ans += x - y
    if y < z:
        ans += z - y
    else:
        ans += y - z

    # output
    if x < y < z:
        print(ans)
    else:
        print(-1)

=======
Suggestion 8

def main():
    X,Y,Z = map(int,input().split())
    if X > Y:
        print(Z)
    else:
        print(-1)

=======
Suggestion 9

def main():
    x,y,z = map(int, input().split())
    if x > y:
        print(z + abs(x - y) - 1)
    else:
        print(-1)

=======
Suggestion 10

def main():
    # data load
    x, y, z = map(int, input().split())

    # calc
    if y > x:
        print(-1)
    else:
        print((x-y) // (z+y))
