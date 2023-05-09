Synthesizing 10/10 solutions

=======
Suggestion 1

def problems198_c():
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 == R**2:
        print(1)
    elif X**2 + Y**2 <= R**2*2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5//R)+1)

=======
Suggestion 2

def main():
    R, X, Y = map(int, input().split())
    distance = (X**2 + Y**2)**(1/2)
    if distance < R:
        print(2)
    else:
        print(int(distance//R + (distance % R != 0)))

=======
Suggestion 3

def main():
    R,X,Y = map(int,input().split())
    if (X**2+Y**2)**(1/2) % R == 0:
        print(int((X**2+Y**2)**(1/2)/R))
    else:
        print(int((X**2+Y**2)**(1/2)/R)+1)

=======
Suggestion 4

def main():
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 < R**2:
        print(2)
    else:
        print((X**2 + Y**2)**(1/2)//R + 1)

=======
Suggestion 5

def solve():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) % R**2 == 0:
        print((X**2 + Y**2) // R**2)
    else:
        print((X**2 + Y**2) // R**2 + 1)
solve()

=======
Suggestion 6

def main():
    R, X, Y = map(int, input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print(int((X**2 + Y**2)**(1/2) // R) + 1)

=======
Suggestion 7

def main():
    r, x, y = map(int, input().split())
    distance = (x**2 + y**2)**(1/2)
    if distance%r == 0:
        print(int(distance//r))
    elif distance < r:
        print(2)
    else:
        print(int(distance//r)+1)

=======
Suggestion 8

def main():
    import math
    R,X,Y = map(int,input().split())
    distance = math.sqrt(X*X + Y*Y)
    if distance == R:
        print(1)
    elif distance <= 2*R:
        print(2)
    else:
        print(math.ceil(distance/R))

=======
Suggestion 9

def solve():
    R,X,Y = map(int,input().split())
    if X**2+Y**2 < R**2:
        return 2
    else:
        return -(-(X**2+Y**2)**(1/2)//R)
print(solve())

=======
Suggestion 10

def solve():
    import sys
    import math
    input = sys.stdin.readline
    R,X,Y = map(int, input().split())
    dist = math.sqrt(X*X+Y*Y)
    if dist == R:
        return 1
    elif dist < R:
        return 2
    else:
        return math.ceil(dist/R)

print(solve())
