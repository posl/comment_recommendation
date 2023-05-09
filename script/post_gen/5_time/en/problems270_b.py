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
    if y > x:
        print(-1)
    else:
        print((x-z)//(y+z))

=======
Suggestion 3

def main():
    x,y,z = map(int, input().split())
    if x > y:
        if y + z >= x:
            print(0)
        else:
            print(-1)
    else:
        if x + z >= y:
            print(0)
        else:
            print(-1)

=======
Suggestion 4

def main():
    x, y, z = map(int, input().split())
    if x < y:
        if y < z:
            print(-1)
        else:
            print(x + z)
    else:
        if z < y:
            print(-1)
        else:
            print(x + z)

=======
Suggestion 5

def problems270_b():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(-1)
    else:
        print(x - z - y)

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if z < y < x:
        print(x + z - y)
    else:
        print(-1)

=======
Suggestion 7

def main():
    x, y, z = map(int, input().split())
    if x > y and y > z:
        print('{}'.format(x - z))
    else:
        print('-1')

=======
Suggestion 8

def main():
    x,y,z = map(int, input().split())
    if x > y:
        print(x-z-y)
    else:
        print(-1)

=======
Suggestion 9

def solve(x, y, z):
    if x < z:
        return -1
    return (x - z) - y

=======
Suggestion 10

def calc_distance(x,y,z):
    if x > y and y > z:
        return x - z
    else:
        return -1
