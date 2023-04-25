Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    R, X, Y = map(int, input().split())
    d = (X ** 2 + Y ** 2) ** 0.5
    if d % R == 0:
        print(int(d / R))
    else:
        print(int(d / R) + 1)

=======
Suggestion 2

def distance(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

=======
Suggestion 3

def main():
    R, X, Y = map(int, input().split())
    d = ((X ** 2) + (Y ** 2)) ** 0.5
    if d % R == 0:
        print(int(d / R))
    else:
        print(int(d / R) + 1)

=======
Suggestion 4

def main():
    R, X, Y = map(int, input().split())
    distance = (X**2 + Y**2)**(1/2)
    if distance % R == 0:
        print(int(distance // R))
    else:
        print(int(distance // R) + 1)

=======
Suggestion 5

def main():
    R, X, Y = map(int, input().split())
    D = (X**2 + Y**2)**(1/2)
    if D < R:
        print(2)
    else:
        print(int(D // R) + (0 if D % R == 0 else 1))

=======
Suggestion 6

def main():
    R, X, Y = map(int, input().split())
    D = (X ** 2 + Y ** 2) ** 0.5
    if D < R:
        print(2)
        return
    print(int(D // R + (D % R > 0)))

main()

=======
Suggestion 7

def main():
    r, x, y = map(int, input().split())
    dist = (x**2 + y**2)**0.5
    if dist % r == 0:
        print(int(dist/r))
    else:
        print(int(dist/r + 1))

main()

=======
Suggestion 8

def main():
    R, X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        print(0)
    else:
        dist = (X ** 2 + Y ** 2) ** 0.5
        if dist % R == 0:
            print(int(dist / R))
        else:
            print(int(dist // R) + 1)

=======
Suggestion 9

def main():
    R, X, Y = map(int, input().split())
    distance = (X ** 2 + Y ** 2) ** 0.5
    steps = (distance / R)
    if steps.is_integer():
        print(int(steps))
    else:
        print(int(steps) + 1)

=======
Suggestion 10

def dist(x, y):
    return ((x**2)+(y**2))**(1/2)
