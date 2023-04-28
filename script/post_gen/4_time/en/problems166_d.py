Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 2

def main():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 3

def main():
    X = int(input())
    for A in range(-200, 200):
        for B in range(-200, 200):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 4

def main():
    x = int(input())
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a**5 - b**5 == x:
                print(a, b)
                return

=======
Suggestion 5

def main():
    X = int(input())
    for A in range(-1000, 1000):
        for B in range(-1000, 1000):
            if A**5 - B**5 == X:
                print(A, B)
                return

=======
Suggestion 6

def main():
    X = int(input())
    for A in range(-1000, 1001):
        for B in range(-1000, 1001):
            if A**5 - B**5 == X:
                print(A, B)
                exit()

=======
Suggestion 7

def main():
    X = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == X:
                print(a, b)
                return

=======
Suggestion 8

def main():
    x = int(input())
    a = 0
    b = 0
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if i**5 - j**5 == x:
                a = i
                b = j
                break
    print("{} {}".format(a, b))

=======
Suggestion 9

def problem_statement():
    """
    Give a pair of integers (A, B) such that A^5-B^5 = X.
    It is guaranteed that there exists such a pair for the given integer X.

    Constraints
    1 ≦ X ≦ 10^9
    X is an integer.
    There exists a pair of integers (A, B) satisfying the condition in Problem Statement.

    Input
    Input is given from Standard Input in the following format:
    X

    Output
    Print A and B, with space in between.
    If there are multiple pairs of integers (A, B) satisfying the condition, you may print any of them.
    A B

    Sample Input 1
    33

    Sample Output 1
    2 -1
    For A=2 and B=-1, A^5-B^5 = 33.

    Sample Input 2
    1

    Sample Output 2
    0 -1
    """
    pass
