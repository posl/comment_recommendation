Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    for A in range(-1000, 1001):
        for B in range(-1000, 1001):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 2

def main():
    X = int(input())
    for i in range(-1000,1001):
        for j in range(-1000,1001):
            if i**5-j**5 == X:
                print(i,j)
                exit()

=======
Suggestion 3

def main():
    x = int(input())
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            if a**5-b**5 == x:
                print(a,b)
                return

=======
Suggestion 4

def main():
    X = int(input())
    for a in range(-118,119):
        for b in range(-119,118):
            if a**5 - b**5 == X:
                print(a,b)
                return

=======
Suggestion 5

def main():
    x = int(input())
    for a in range(10**5):
        for b in range(10**5):
            if a**5-b**5 == x:
                print(a,b)
                return

=======
Suggestion 6

def main():
    x = int(input())
    for i in range(-300, 300):
        for j in range(-300, 300):
            if i**5-j**5 == x:
                print(i, j)
                return
main()

=======
Suggestion 7

def main():
    X = int(input())
    A = 0
    B = 0
    for a in range(0, 1000):
        for b in range(0, 1000):
            if a**5-b**5 == X:
                A = a
                B = -b
            elif a**5-b**5 == -X:
                A = a
                B = b
    print(A, B)
main()

=======
Suggestion 8

def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1, 10**6):
        if i**5 - (i-1)**5 == X:
            A = i
            B = i-1
            break
    print(A, B)
