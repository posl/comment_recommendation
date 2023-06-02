Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y,z = map(int, input().split())
    if y > 0:
        print(-1)
    else:
        print(abs(x) + abs(z))

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if x < y and x < z:
        print(-1)
    else:
        print(abs(y - z) + x)

=======
Suggestion 3

def main():
    x,y,z = map(int,input().split())
    if x > 0 and y < 0 and z > 0:
        print(-1)
    elif x < 0 and y > 0 and z < 0:
        print(-1)
    else:
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        print(x+y+z)

=======
Suggestion 4

def solution(x, y, z):
    if y > 0 and z > 0:
        return -1
    elif y < 0 and z < 0:
        return -1
    else:
        return abs(y - z)

=======
Suggestion 5

def main():
    x, y, z = map(int, input().split())
    if y > z:
        print(-1)
    else:
        print((x * z) // y)

=======
Suggestion 6

def main():
    x,y,z = map(int, input().split())
    if y > x:
        print(-1)
    else:
        print((x+z)//(y+z)*y)

=======
Suggestion 7

def solve(x,y,z):
    if (y-x)*(z-y) > 0:
        return abs(y-x)
    else:
        return -1

=======
Suggestion 8

def main():
    x, y, z = list(map(int, input().split()))
    if x < y < z or x > y > z:
        print(-1)
    else:
        print(abs(x-z) + abs(x-y))

=======
Suggestion 9

def problems270_b():
    x,y,z = map(int,input().split())
    if (x > 0 and y > 0 and z > 0) or (x < 0 and y < 0 and z < 0) or (x > 0 and y < 0 and z < 0) or (x < 0 and y > 0 and z > 0):
        print(-1)
    else:
        if x > 0:
            print(x + abs(y) + z)
        else:
            print(abs(x) + y + abs(z))

=======
Suggestion 10

def main():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(-1)
    else:
        print(abs(x - z) + abs(z - y))
