Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    if a == 1 and b == 2:
        print(3)
    elif a == 1 and b == 3:
        print(2)
    elif a == 2 and b == 1:
        print(3)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 1:
        print(2)
    elif a == 3 and b == 2:
        print(1)
    else:
        print("error")

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    if A == 1:
        if B == 2:
            print(3)
        else:
            print(2)
    elif A == 2:
        if B == 1:
            print(3)
        else:
            print(1)
    else:
        if B == 1:
            print(2)
        else:
            print(1)

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = 0
    if a == 1:
        if b == 2:
            c = 3
        elif b == 3:
            c = 2
    elif a == 2:
        if b == 1:
            c = 3
        elif b == 3:
            c = 1
    elif a == 3:
        if b == 1:
            c = 2
        elif b == 2:
            c = 1
    print(c)

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = [1,2,3]
    c.remove(a)
    c.remove(b)
    print(c[0])

=======
Suggestion 6

def main():
    A = int(input())
    B = int(input())
    print(6 - A - B)

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())

    print(6-a-b)

main()
