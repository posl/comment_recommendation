Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    for a in range(-118, 119):
        for b in range(-119, 118):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 2

def solve(x):
    for a in range(0, 1001):
        for b in range(0, 1001):
            if a**5 - b**5 == x:
                return a, b

x = int(input())
a, b = solve(x)
print(a, b)

=======
Suggestion 3

def main():
    x = int(input())
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 4

def main():
    x = input()
    x = int(x)
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5 - b**5 == x:
                print(a,b)
                return

=======
Suggestion 5

def main():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 6

def main():
    x = int(input())
    for a in range(1, 1000):
        for b in range(-1000, 1000):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 7

def main():
    X = int(input())
    for A in range(-118, 120):
        for B in range(-119, 119):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 8

def main():
    X = int(input())
    for A in range(-120,120):
        for B in range(-120,120):
            if A**5 - B**5 == X:
                print(A,B)
                return

=======
Suggestion 9

def getAB(x):
    for a in range(0, 1000):
        for b in range(-1000, 1000):
            if a**5 - b**5 == x:
                return a, b
