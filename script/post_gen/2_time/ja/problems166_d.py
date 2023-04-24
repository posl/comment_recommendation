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
    X = int(input())
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            if a ** 5 - b ** 5 == X:
                print(a, b)
                return

=======
Suggestion 3

def main():
    x = int(input())
    for a in range(-200, 201):
        for b in range(-200, 201):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 4

def main():
    X = int(input())
    for A in range(-118,120):
        for B in range(-119,120):
            if A**5 - B**5 == X:
                print(A,B)
                return

=======
Suggestion 5

def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            if i**5 - j**5 == X:
                A = i
                B = j
                break
    print(A,B)

=======
Suggestion 6

def main():
    X = int(input())
    for A in range(1, 1000):
        for B in range(1, 1000):
            if A ** 5 - B ** 5 == X:
                print(A, B)
                return

=======
Suggestion 7

def main():
    x = int(input())
    a = 0
    b = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i ** 5 - j ** 5 == x:
                a = i
                b = -j
            elif i ** 5 + j ** 5 == x:
                a = i
                b = j
    print(a, b)

=======
Suggestion 8

def main():
    X = int(input())
    #print(X)
    for i in range(10**5):
        for j in range(10**5):
            if i**5-j**5 == X:
                print(i,j)
                return
            elif i**5-j**5 == -X:
                print(-i,j)
                return

=======
Suggestion 9

def main():
    X = int(input())
    # 0 0 0 0 0
    # 1 0 0 0 0
    # 0 1 0 0 0
    # 0 0 1 0 0
    # 0 0 0 1 0
    # 0 0 0 0 1
    # 1 1 1 1 1
    # 2 1 1 1 1
    # 1 2 1 1 1
    # 1 1 2 1 1
    # 1 1 1 2 1
    # 1 1 1 1 2
    # 2 2 2 2 2
    # 3 2 2 2 2
    # 2 3 2 2 2
    # 2 2 3 2 2
    # 2 2 2 3 2
    # 2 2 2 2 3
    # 3 3 3 3 3
    # 4 3 3 3 3
    # 3 4 3 3 3
    # 3 3 4 3 3
    # 3 3 3 4 3
    # 3 3 3 3 4
    # 4 4 4 4 4
    # 5 4 4 4 4
    # 4 5 4 4 4
    # 4 4 5 4 4
    # 4 4 4 5 4
    # 4 4 4 4 5
    # 5 5 5 5 5
    # 6 5 5 5 5
    # 5 6 5 5 5
    # 5 5 6 5 5
    # 5 5 5 6 5
    # 5 5 5 5 6
    # 6 6 6 6 6
    # 7 6 6 6
