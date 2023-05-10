Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print(7-a-b)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print(0)
    elif a == 1 and b == 2:
        print(3)
    elif a == 5 and b == 3:
        print(7)
    else:
        print(1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        print(3)
    elif a != 1 and b != 1:
        print(1)
    elif a != 2 and b != 2:
        print(2)
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print(0)
    elif a == 0 or b == 0:
        print(3)
    elif a == 1 and b == 1:
        print(2)
    elif a == 1 or b == 1:
        print(1)
    elif a == 2 and b == 2:
        print(0)
    elif a == 2 or b == 2:
        print(1)
    elif a == 3 and b == 3:
        print(0)
    elif a == 3 or b == 3:
        print(1)
    elif a == 4 and b == 4:
        print(0)
    elif a == 4 or b == 4:
        print(1)
    elif a == 5 and b == 5:
        print(0)
    elif a == 5 or b == 5:
        print(1)
    elif a == 6 and b == 6:
        print(0)
    elif a == 6 or b == 6:
        print(1)
    elif a == 7 and b == 7:
        print(0)
    elif a == 7 or b == 7:
        print(1)

=======
Suggestion 5

def problems270_a(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 1
    elif a == 1 and b == 1:
        return 2
    elif a == 2 and b == 0:
        return 2
    elif a == 0 and b == 2:
        return 2
    elif a == 2 and b == 1:
        return 3
    elif a == 1 and b == 2:
        return 3
    elif a == 2 and b == 2:
        return 4
    elif a == 3 and b == 0:
        return 3
    elif a == 0 and b == 3:
        return 3
    elif a == 3 and b == 1:
        return 4
    elif a == 1 and b == 3:
        return 4
    elif a == 3 and b == 2:
        return 5
    elif a == 2 and b == 3:
        return 5
    elif a == 3 and b == 3:
        return 6
    elif a == 4 and b == 0:
        return 4
    elif a == 0 and b == 4:
        return 4
    elif a == 4 and b == 1:
        return 5
    elif a == 1 and b == 4:
        return 5
    elif a == 4 and b == 2:
        return 6
    elif a == 2 and b == 4:
        return 6
    elif a == 4 and b == 3:
        return 7
    elif a == 3 and b == 4:
        return 7
    elif a == 4 and b == 4:
        return 8

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        print(0)
    elif A == 1 and B == 0:
        print(2)
    elif A == 0 and B == 1:
        print(2)
    elif A == 2 and B == 0:
        print(4)
    elif A == 0 and B == 2:
        print(4)
    elif A == 1 and B == 1:
        print(3)
    elif A == 2 and B == 1:
        print(5)
    elif A == 1 and B == 2:
        print(5)
    elif A == 2 and B == 2:
        print(6)
    elif A == 3 and B == 0:
        print(6)
    elif A == 0 and B == 3:
        print(6)
    elif A == 3 and B == 1:
        print(7)
    elif A == 1 and B == 3:
        print(7)
    elif A == 3 and B == 2:
        print(8)
    elif A == 2 and B == 3:
        print(8)
    elif A == 3 and B == 3:
        print(9)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print(0)
    elif a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        print(3 - a - b)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(3 - a - b)
