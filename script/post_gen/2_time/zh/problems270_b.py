Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y,z = map(int, input().split())
    if y > z:
        print(-1)
    else:
        print((x*y)//(z-y))

=======
Suggestion 2

def problem270_b():
    x,y,z = map(int,input().split())
    if x > y > z or x > z > y:
        print(-1)
    else:
        print(x + z)

=======
Suggestion 3

def solve(x, y, z):
    if x > y and y > z:
        return x - z
    else:
        return -1

=======
Suggestion 4

def main():
    x,y,z = map(int,input().split())
    if (x*y*z) == 0:
        print(-1)
    elif x*y*z > 0:
        print(-1)
    else:
        print(abs(x-y)+abs(y-z)+abs(z-x))

=======
Suggestion 5

def solve(x,y,z):
    if (x>0 and y>0 and z>0) or (x<0 and y<0 and z<0):
        return -1
    elif x>0 and y>0 and z<0:
        return abs(x-y)
    elif x>0 and y<0 and z>0:
        return x+y
    elif x<0 and y>0 and z>0:
        return y+z
    elif x<0 and y<0 and z>0:
        return abs(x-z)
    elif x<0 and y>0 and z<0:
        return abs(x-y)+abs(y-z)
    elif x>0 and y<0 and z<0:
        return abs(x-z)
    else:
        return abs(x-y)+abs(y-z)

=======
Suggestion 6

def solve(x, y, z):
    if y > 0 and z > 0:
        return -1
    if y < 0 and z < 0:
        return -1
    if y > 0 and y > z:
        return -1
    if y < 0 and y < z:
        return -1
    return abs(x - y)

=======
Suggestion 7

def main():
    x,y,z = map(int,input().split())
    if x < y < z:
        print(z-y)
    else:
        print(-1)
main()

=======
Suggestion 8

def main():
    x,y,z = map(int, input().split())
    if x > y > z:
        print(x - z + y - z)
    elif x > z > y:
        print(x - y + z - y)
    elif y > x > z:
        print(y - z + x - z)
    elif y > z > x:
        print(y - x + z - x)
    elif z > x > y:
        print(z - y + x - y)
    elif z > y > x:
        print(z - x + y - x)
    else:
        print(-1)

=======
Suggestion 9

def main():
    x,y,z = map(int, input().split())
    if x < y:
        print(-1)
    else:
        print(x+y+z)

=======
Suggestion 10

def problems270_b():
    x,y,z = map(int, input().split())
    if y > 0 or z > 0:
        print(-1)
    else:
        print(x - y - z)
