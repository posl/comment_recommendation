Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    if A == 1 and B == 2:
        print(3)
    elif A == 1 and B == 3:
        print(2)
    elif A == 2 and B == 1:
        print(3)
    elif A == 2 and B == 3:
        print(1)
    elif A == 3 and B == 1:
        print(2)
    elif A == 3 and B == 2:
        print(1)

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    if a == 1:
        if b == 2:
            print(3)
        else:
            print(2)
    else:
        if b == 1:
            print(3)
        else:
            print(1)

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    C = 0
    if A == 1:
        if B == 2:
            C = 3
        elif B == 3:
            C = 2
    elif A == 2:
        if B == 1:
            C = 3
        elif B == 3:
            C = 1
    elif A == 3:
        if B == 1:
            C = 2
        elif B == 2:
            C = 1
    print(C)

main()

=======
Suggestion 4

def main():
    A = int(input())
    B = int(input())
    print(6 - A - B)

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    print(6 - a - b)
