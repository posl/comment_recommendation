Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1 + x2 + y2) % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    if (x2 - x1) % 2 == 0 and (y2 - y1) % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x1 - dy
    y4 = y1 + dx
    if (x3 - x1) ** 2 + (y3 - y1) ** 2 == (x3 - x2) ** 2 + (y3 - y2) ** 2 and \
       (x4 - x1) ** 2 + (y4 - y1) ** 2 == (x4 - x2) ** 2 + (y4 - y2) ** 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2)**2 + (y1 - y2)**2 in [5, 10]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def lattice_point(x1, y1, x2, y2):
    if (x1 == x2 and y1 == y2):
        return "No"
    #check if (x1, y1) is a lattice point
    if ((x1**2 + y1**2)**0.5).is_integer():
        return "Yes"
    #check if (x2, y2) is a lattice point
    if ((x2**2 + y2**2)**0.5).is_integer():
        return "Yes"
    #if (x1, y1) and (x2, y2) are both lattice points, then a point (x, y) is a lattice point if and only if
    #x = x1 + a(x2 - x1) and y = y1 + a(y2 - y1) where a is an integer
    #if (x1, y1) and (x2, y2) are not both lattice points, then a point (x, y) is a lattice point if and only if
    #x = x1 + a(x2 - x1) and y = y1 + a(y2 - y1) where a is an integer and a is not 0
    #if a is 0, then (x, y) = (x1, y1) or (x, y) = (x2, y2)
    #if a is not 0, then (x, y) = (x1, y1) + a(x2 - x1, y2 - y1)
    #if (x1, y1) is a lattice point, then (x1, y1) + a(x2 - x1, y2 - y1) is a lattice point
    #if (x2, y2) is a lattice point, then (x1, y1) + a(x2 - x1, y2 - y1) is a lattice point
    #if (x1, y1) and (x2, y2) are both not lattice points, then (x1, y1) + a(x2 - x1, y2 - y1) is a lattice point
    #if (x1, y1) and (x2, y2) are both not lattice points
