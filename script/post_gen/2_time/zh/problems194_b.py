Synthesizing 10/10 solutions

=======
Suggestion 1

def icecream_type(A,B):
    if A+B>=15 and B>=8:
        return 1
    elif A+B>=10 and B>=3:
        return 2
    elif A+B>=3:
        return 3
    else:
        return 4

=======
Suggestion 2

def icecream(a,b):
    if a+b>=15 and b>=8:
        print(1)
    elif a+b>=10 and b>=3:
        print(2)
    elif a+b<10 and b>=3:
        print(3)
    else:
        print(4)

=======
Suggestion 3

def icecream(a,b):
    if a+b >= 15 and b >= 8:
        return 1
    elif a+b >= 10 and b >= 3:
        return 2
    elif a+b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 4

def icecream_type(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 5

def solve(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A+B>=15 and B>=8:
        print(1)
    elif A+B>=10 and B>=3:
        print(2)
    elif A+B>=3:
        print(3)
    else:
        print(4)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a + b >= 15 and b >= 8:
        print(1)
    elif a + b >= 10 and b >= 3:
        print(2)
    elif a + b >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if A == 0:
        print(4)
    elif B == 0:
        print(3)
    elif A + B < 15:
        print(4)
    elif A + B >= 15 and B >= 8:
        print(1)
    elif A + B >= 10 and B >= 3:
        print(2)
    else:
        print(4)

=======
Suggestion 9

def icecream(a, b):
    if a+b >= 15 and b >= 8:
        return 1
    elif a+b >= 10 and b >= 3:
        return 2
    elif a+b < 10 and b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 10

def icecream(a,b):
    if a+b >= 15 and b >= 8:
        return 1
    if a+b >= 10 and b >= 3:
        return 2
    if a+b < 10 and b >= 3:
        return 3
    return 4
