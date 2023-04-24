Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            if i ** 5 - j ** 5 == x:
                print(i, j)
                return

=======
Suggestion 2

def main():
    X = int(input())
    for A in range(-1000, 1000):
        for B in range(-1000, 1000):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 3

def main():
    X = int(input())
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            if i ** 5 - j ** 5 == X:
                print(i, j)
                exit(0)

=======
Suggestion 4

def main():
    x = int(input())
    for i in range(-120, 120):
        for j in range(-120, 120):
            if i**5 - j**5 == x:
                print(i, j)
                return

=======
Suggestion 5

def main():
    x = int(input())
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            if a**5-b**5 == x:
                print(a,b)
                exit()
main()

=======
Suggestion 6

def main():
    X = int(input())
    for i in range(-118,120):
        for j in range(-118,120):
            if i**5-j**5 == X:
                print(i,j)
                return

main()

=======
Suggestion 7

def main():
    X = int(input())
    i = 0
    while i**5 < X:
        j = 0
        while j**5 < X:
            if i**5 - j**5 == X:
                print(i, -j)
                return
            j += 1
        i += 1

=======
Suggestion 8

def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i**5 - j**5 == X:
                A = i
                B = j
                break
    print(A, B)

=======
Suggestion 9

def solve():
    X = int(input())
    # X = 33
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            if a**5 - b**5 == X:
                print(a, b)
                return

solve()

=======
Suggestion 10

def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1,1000):
        A = i
        B = i ** 5 - X
        if B ** 5 == A:
            break
    print(A,B)
