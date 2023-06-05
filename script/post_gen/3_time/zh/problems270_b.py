Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y,z = map(int,input().split())
    if (x > y and y > z) or (x < y and y < z):
        print(-1)
    else:
        print(abs(x-z)+abs(y-z))

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    if (x > y) and (y > z):
        print(x - z)
    else:
        print(-1)

=======
Suggestion 3

def main():
    x, y, z = map(int, input().split())
    print(x + z if x < y < z else -1)

=======
Suggestion 4

def problems270_b(x,y,z):
    if x > 0 and y > 0 and z > 0:
        return -1
    elif x < 0 and y < 0 and z < 0:
        return -1
    elif x > 0 and y < 0 and z < 0:
        return -1
    elif x < 0 and y > 0 and z > 0:
        return -1
    elif x > 0 and y > 0 and z < 0:
        return -1
    elif x > 0 and y < 0 and z > 0:
        return -1
    elif x < 0 and y > 0 and z < 0:
        return -1
    elif x < 0 and y < 0 and z > 0:
        return -1
    else:
        return abs(x - y) + abs(y - z)

print(problems270_b(10,-10,1))
print(problems270_b(20,10,-10))
print(problems270_b(100,1,1000))

=======
Suggestion 5

def get_distance(x, y, z):
    if x < z:
        return -1
    return x - z + y

=======
Suggestion 6

def problem270_b(x,y,z):
    if z>y:
        return -1
    return x+y+z

print(problem270_b(10,-10,1))
print(problem270_b(20,10,-10))
print(problem270_b(100,1,1000))

=======
Suggestion 7

def main():
    x,y,z=map(int,input().split())
    if x>y>z:
        print(x-y+z)
    else:
        print(-1)

=======
Suggestion 8

def solve():
    x,y,z = map(int, input().split())
    if y < z:
        print(-1)
    else:
        print( (x*z)//(y-z) )

=======
Suggestion 9

def main():
    #输入
    X,Y,Z = map(int,input().split())
    #判断
    if (X > Y and Y > Z) or (X < Y and Y < Z):
        print(-1)
    else:
        print(abs(X-Z)+abs(Z-Y))

=======
Suggestion 10

def main():
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    if x > y and x > z:
        if y < z:
            print(x - y)
        else:
            print(x - z)
    elif y > x and y > z:
        if x < z:
            print(y - x)
        else:
            print(y - z)
    elif z > x and z > y:
        if x < y:
            print(z - x)
        else:
            print(z - y)
    else:
        print(-1)
