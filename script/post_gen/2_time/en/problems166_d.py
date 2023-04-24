Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 2

def main():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                return

=======
Suggestion 3

def main():
    x = int(input())
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            if i**5 - j**5 == x:
                print(i, j)
                return

=======
Suggestion 4

def main():
    X = int(input())
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            if i**5 - j**5 == X:
                print(i, j)
                exit()

=======
Suggestion 5

def main():
    x = int(input())
    for i in range(-200, 200):
        for j in range(-200, 200):
            if i**5 - j**5 == x:
                print(i, j)
                return

main()

=======
Suggestion 6

def main():
    X = int(input())
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            if a**5-b**5 == X:
                print(a, b)
                return

=======
Suggestion 7

def main():
    x = int(input())
    a, b = 0, 0
    for i in range(-200, 200):
        for j in range(-200, 200):
            if i**5 - j**5 == x:
                a, b = i, j
                break
    print(a, b)

=======
Suggestion 8

def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1000):
        for j in range(1000):
            if i**5 - j**5 == X:
                A = i
                B = j
    print(A, B)

=======
Suggestion 9

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    if n % 10 not in (0, 1, 4, 5, 6, 9):
        return False
    if n < 1024:
        return int(n ** 0.5) ** 2 == n
    r = int(n ** 0.5)
    return (r - 1) ** 2 < n <= r ** 2
