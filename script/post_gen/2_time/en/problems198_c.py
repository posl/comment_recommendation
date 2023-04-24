Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

=======
Suggestion 2

def distance(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)

=======
Suggestion 3

def main():
    R, X, Y = map(int, input().split())
    dist = (X**2 + Y**2)**(1/2)
    if dist % R == 0:
        print(int(dist/R))
    else:
        print(int(dist//R)+1)

=======
Suggestion 4

def main():
    R, X, Y = map(int, input().split())
    dist = ((X ** 2) + (Y ** 2)) ** (1/2)
    if dist % R == 0:
        print(int(dist / R))
    else:
        print(int(dist // R + 1))

=======
Suggestion 5

def main():
    R, X, Y = map(int, input().split())
    d = (X**2 + Y**2)**0.5
    if d == R:
        print(1)
    elif d < R:
        print(2)
    else:
        print(int(d/R) + (1 if d % R else 0))

=======
Suggestion 6

def main():
    R, X, Y = map(int, input().split())
    distance = (X**2 + Y**2)**(1/2)
    if distance == R:
        print(1)
    elif distance < R:
        print(2)
    else:
        print(int(distance//R) + (1 if distance % R else 0))

main()

=======
Suggestion 7

def main():
    R, X, Y = map(int,input().split())
    if X**2 + Y**2 == R**2:
        print(1)
    elif X**2 + Y**2 < R**2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5 // R) + (1 if (X**2 + Y**2)**0.5 % R else 0))

=======
Suggestion 8

def main():
    r, x, y = map(int, input().split())
    if x % r == 0 and y % r == 0:
        print(abs(x//r) + abs(y//r))
    else:
        print(abs(x//r) + abs(y//r) + 1)

=======
Suggestion 9

def dist(x, y):
    return (x**2 + y**2)**(1/2)
