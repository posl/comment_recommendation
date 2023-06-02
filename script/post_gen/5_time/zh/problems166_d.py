Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                exit()

=======
Suggestion 2

def main():
    x = int(input())
    for a in range(-120,120):
        for b in range(-120,120):
            if a**5-b**5 == x:
                print(a,b)
                return

=======
Suggestion 3

def main():
    X = int(input())
    for i in range(1, 1000):
        for j in range(-1000, 1000):
            if i ** 5 - j ** 5 == X:
                print(i, j)
                return

=======
Suggestion 4

def findAB(x):
    for a in range(1, 1001):
        for b in range(1, 1001):
            if a ** 5 - b ** 5 == x:
                return a, b
            if a ** 5 + b ** 5 == x:
                return a, -b
    return None, None

while True:
    try:
        x = int(input())
        a, b = findAB(x)
        print(a, b)
    except:
        break

=======
Suggestion 5

def problem_166(x):
    for b in range(-1000,1000):
        for a in range(-1000,1000):
            if a**5 - b**5 == x:
                return (a,b)

=======
Suggestion 6

def main():
    x = int(input())
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 7

def solve():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 8

def main():
    x = int(input())
    for a in range(-118,119):
        for b in range(-119,118):
            if a**5 - b**5 == x:
                print(a,b)
                return
