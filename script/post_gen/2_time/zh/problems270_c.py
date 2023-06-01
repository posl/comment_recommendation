Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y,z = map(int,input().split())
    if y > 0:
        print(-1)
    else:
        print(abs(x)+abs(z))

=======
Suggestion 2

def solve(x,y,z):
    if y > z:
        return -1
    else:
        return abs(x-y)+abs(y-z)

=======
Suggestion 3

def problems270_b():
    x,y,z = map(int,input().split())
    if x>y:
        print(x-z+y)
    else:
        print(-1)
problems270_b()

=======
Suggestion 4

def main():
    input_list = input().split()
    x = int(input_list[0])
    y = int(input_list[1])
    z = int(input_list[2])
    if (x > 0 and x > y) or (x < 0 and x < y):
        print(abs(x - y) + abs(y - z))
    else:
        print(-1)

=======
Suggestion 5

def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(z + x - y)
    else:
        print(-1)

=======
Suggestion 6

def main():
    x, y, z = map(int, input().split())
    if y > x:
        print(-1)
    else:
        print((x+y)//(y-z))

=======
Suggestion 7

def solve():
    x,y,z = map(int, input().split())
    if x > y:
        print(z + x - y)
    else:
        print(-1)

=======
Suggestion 8

def main():
    x,y,z = map(int,input().split())
    if y*z > 0:
        if abs(x) > abs(y):
            print(abs(x-y))
        else:
            print(abs(y-x))
    else:
        print(-1)

=======
Suggestion 9

def solution(x,y,z):
    if y>z:
        return -1
    else:
        return abs(z-x)

x,y,z=map(int,input().split())
print(solution(x,y,z))

=======
Suggestion 10

def main():
    x,y,z = map(int, input().split())
    if y > z:
        print(-1)
    else:
        print(int((y/x)*z))
