Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    a = int(input())
    b = int(input())
    print(6-(a+b))

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    if a == 1 and b == 2:
        print(3)
    elif a == 2 and b == 1:
        print(3)
    elif a == 1 and b == 3:
        print(2)
    elif a == 3 and b == 1:
        print(2)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 2:
        print(1)

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    if A == 1 and B == 2:
        print(3)
    elif A == 2 and B == 1:
        print(3)
    elif A == 3 and B == 1:
        print(2)
    elif A == 1 and B == 3:
        print(2)
    elif A == 2 and B == 3:
        print(1)
    elif A == 3 and B == 2:
        print(1)

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    if a == 1:
        if b == 2:
            print(3)
        else:
            print(2)
    elif a == 2:
        if b == 1:
            print(3)
        else:
            print(1)
    else:
        if b == 1:
            print(2)
        else:
            print(1)

=======
Suggestion 5

def answer(A, B):
    if A == 1 and B == 2:
        return 3
    elif A == 2 and B == 3:
        return 1
    elif A == 3 and B == 1:
        return 2
    elif A == 1 and B == 3:
        return 2
    elif A == 2 and B == 1:
        return 3
    elif A == 3 and B == 2:
        return 1

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    print(6-a-b)

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())

    if a == b:
        print(3)
    elif a != 1 and b != 1:
        print(1)
    elif a != 2 and b != 2:
        print(2)
    else:
        print(3)

=======
Suggestion 8

def main():
    a = int(input())
    b = int(input())
    if a == 1:
        if b == 2:
            print(3)
        elif b == 3:
            print(2)
    elif a == 2:
        if b == 1:
            print(3)
        elif b == 3:
            print(1)
    elif a == 3:
        if b == 1:
            print(2)
        elif b == 2:
            print(1)
