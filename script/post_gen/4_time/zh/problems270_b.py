Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if (x > 0 and y > 0 and z > 0) or (x < 0 and y < 0 and z < 0):
        print(-1)
    else:
        if x > 0:
            print(z + x - y)
        else:
            print(z + y - x)

=======
Suggestion 2

def solution():
    x, y, z = map(int, input().split())
    if x < y:
        print(-1)
    else:
        print(x + y + z)

=======
Suggestion 3

def main():
    x,y,z = map(int, input().split())

    if x > y:
        print(-1)
    else:
        print(int((x+z)/(z-y)))

=======
Suggestion 4

def solve(x,y,z):
    if y>0 and y<z:
        return -1
    else:
        return abs(x-z)

=======
Suggestion 5

def solve(x,y,z):
    if x*z > 0:
        return abs(x-y)
    else:
        return abs(x+y)

=======
Suggestion 6

def main():
    x,y,z = map(int, input().split())
    if (x > y and y > z) or (x < y and y < z):
        print(-1)
        return

    if x > y:
        print(x - z)
    else:
        print(z - x)

=======
Suggestion 7

def solve(x, y, z):
    if x > 0 and y < 0 and z < 0 and x + y < 0:
        return -1
    if x < 0 and y > 0 and z > 0 and x + y > 0:
        return -1
    return abs(x - z) + abs(y)

=======
Suggestion 8

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(x - y + z)
    else:
        print(-1)

=======
Suggestion 9

def main():
    x,y,z = map(int,input().split())
    if x < y < z:
        print(z-x)
    else:
        print(-1)

=======
Suggestion 10

def solve():
    X, Y, Z = map(int, input().split())
    if Y > Z:
        print(-1)
    else:
        print((X * Z) // (Z - Y))

solve()
