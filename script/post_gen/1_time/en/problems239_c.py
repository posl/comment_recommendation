Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        print("Yes")
        return
    elif y1 == y2:
        print("Yes")
        return
    elif abs(x1 - x2) == abs(y1 - y2):
        print("Yes")
        return
    else:
        print("No")

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) == (x2, y2):
        print("No")
        return
    if (x1 - x2) % 2 == 0:
        print("Yes")
        return
    if (y1 - y2) % 2 == 0:
        print("Yes")
        return
    print("No")

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x1 - x2
    y = y1 - y2
    if x * x + y * y == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1 - x2)**2 + (y1 - y2)**2) % 2 == 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    #input
    x1, y1, x2, y2 = map(int, input().split())
    #compute
    #output
    print(['No', 'Yes'][((x1-x2)**2+(y1-y2)**2)**.5%1==0])

=======
Suggestion 9

def lattice_points(x1, y1, x2, y2):
    # This function takes in two points (x1, y1) and (x2, y2) on a 2D plane and returns the number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2).
    # The number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2) is equal to the number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2) is equal to the distance between (x1, y1) and (x2, y2).
    # The number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2) is equal to the number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2) is equal to the distance between (x1, y1) and (x2, y2).
    # The number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2) is equal to the number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (x1, y1) is equal to the distance between (x, y) and (x2, y2) is equal to the distance between (x1, y1) and (x2, y2).
    # The number of lattice points (x, y) that satisfy the condition that the distance between (x, y) and (
