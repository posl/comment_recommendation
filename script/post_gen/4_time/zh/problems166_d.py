Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem166_d(x):
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a ** 5 - b ** 5 == x:
                return a, b
    return 0, 0

x = int(input())
a, b = problem166_d(x)
print(a, b)

=======
Suggestion 2

def main():
    x = int(input())
    for a in range(-118,120):
        for b in range(-119,119):
            if a**5 - b**5 == x:
                print(a,b)
                return

=======
Suggestion 3

def main():
    x = int(input())
    for i in range(-120, 120):
        for j in range(-120, 120):
            if i ** 5 - j ** 5 == x:
                print(i, j)
                return

=======
Suggestion 4

def solve(x):
    a = 0
    b = 0
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if i**5 - j**5 == x:
                a = i
                b = j
                break
        if a != 0:
            break
    return a, b

=======
Suggestion 5

def get_a_b(x):
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            if a**5 - b**5 == x:
                return a, b

x = int(input())
a, b = get_a_b(x)
print(a, b)

=======
Suggestion 6

def problem166_d():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 7

def findAB(x):
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            if i**5-j**5 == x:
                return i,j
    return 0,0

x = int(input())
a,b = findAB(x)
print(a,b)

=======
Suggestion 8

def main():
    x = int(input())
    for a in range(-118, 119):
        for b in range(-119, 118):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 9

def solve(x):
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a ** 5 - b ** 5 == x:
                return a, b

x = int(input())
a, b = solve(x)
print(a, b)
