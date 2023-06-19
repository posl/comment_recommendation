Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def icecream():
    a,b = map(int, input().split())
    if a+b >= 15 and b >= 8:
        print(1)
    elif a+b >= 10 and b >= 3:
        print(2)
    elif a+b >= 3:
        print(3)
    else:
        print(4)

icecream()

=======
Suggestion 2

def icecream_type(a, b):
    if a + b < 15:
        return 4
    elif a >= 10 and b >= 8:
        return 1
    elif a >= 3:
        return 2
    else:
        return 3

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 15 and B >= 8:
        print(1)
    elif A >= 10 and B >= 3:
        print(2)
    elif A >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if A+B >= 15 and B >= 8:
        print(1)
    elif A+B >= 10 and B >= 3:
        print(2)
    elif A+B >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 5

def icecream(a,b):
    if a+b >= 15 and b >= 8:
        print(1)
    elif a+b >= 10 and b >= 3:
        print(2)
    elif a+b < 10 and b >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a+b < 15:
        print(4)
    elif a+b >= 15 and b >= 8:
        print(1)
    elif a+b >= 10 and b >= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 7

def icecream(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 8

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
