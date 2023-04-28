Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(x - y + z)
    else:
        print(-1)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if x > y:
        if y + z >= x:
            print(0)
        else:
            print(-1)
    else:
        if y - z <= x:
            print(0)
        else:
            print(-1)

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        print(X - Y + Z)
    else:
        print(-1)

=======
Suggestion 4

def problems270_b():
    x, y, z = map(int, input().split())
    print((x - z) // (y + z))

=======
Suggestion 5

def main():
    X, Y, Z = map(int, input().split())
    if X > Y and Y > Z:
        print("1")
    elif X > Y and Y < Z:
        print("-1")
    elif X < Y and Y < Z:
        print("-1")
    elif X < Y and Y > Z:
        print("-1")
    elif X > Y and Y == Z:
        print("-1")
    elif X < Y and Y == Z:
        print("-1")
    elif X == Y and Y > Z:
        print("-1")
    elif X == Y and Y < Z:
        print("-1")
    elif X == Y and Y == Z:
        print("-1")
    elif X < Y and Y == Z:
        print("-1")
    elif X > Y and Y == Z:
        print("-1")
    elif X < Y and Y == Z:
        print("-1")
    elif X > Y and Y == Z:
        print("-1")
    else:
        print("0")

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if y < z < x:
        print('{}'.format(x - y + z))
    else:
        print('-1')

=======
Suggestion 7

def main():
    x,y,z = map(int, input().split())
    if x > z and y < z:
        print(abs(x-z)+abs(y-z)+1)
    else:
        print(-1)

=======
Suggestion 8

def main():
    x,y,z = map(int, input().split())
    if y < z:
        print(-1)
    else:
        print((x-z)/(y+z)*y+z)

=======
Suggestion 9

def solve(x,y,z):
    if x > y:
        return x-y+z
    else:
        return -1

=======
Suggestion 10

def input():
    return sys.stdin.readline()[:-1]
