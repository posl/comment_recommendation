Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    for A in range(-200, 200):
        for B in range(-200, 200):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 2

def main():
    X = int(input())
    for A in range(-118,119):
        for B in range(-119,118):
            if A**5 - B**5 == X:
                print(A,B)
                exit()

=======
Suggestion 3

def solve():
    X = int(input())

    for i in range(-200, 200):
        for j in range(-200, 200):
            if i**5 - j**5 == X:
                print(i, j)
                return

=======
Suggestion 4

def main():
    x = int(input())
    for a in range(-200,200):
        for b in range(-200,200):
            if a**5 - b**5 == x:
                print(a,b)
                return

=======
Suggestion 5

def main():
    x = int(input())
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a**5 - b**5 == x:
                print(a, b)
                exit()

=======
Suggestion 6

def main():
    X = int(input())
    for A in range(-1000, 1000):
        for B in range(-1000, 1000):
            if A ** 5 - B ** 5 == X:
                print(A, B)
                return

=======
Suggestion 7

def main():
    x = int(input())
    a = -1
    b = -1
    for i in range(-118,120):
        for j in range(-119,119):
            if i**5 - j**5 == x:
                a = i
                b = j
                break
        if a != -1:
            break
    print(a,b)

=======
Suggestion 8

def main():
    x = int(input())
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5 - b**5 == x:
                print(a,b)
                return
