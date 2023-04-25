Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A + B >= 15 and B >= 8:
        print(1)
    elif A + B >= 10 and B >= 3:
        print(2)
    elif A + B >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a + b) >= 15 and b >= 8:
        print(1)
    elif (a + b) >= 10 and b >= 3:
        print(2)
    elif (a + b) >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if 15 <= a + b and 8 <= b:
        print(1)
    elif 10 <= a + b and 3 <= b:
        print(2)
    elif 3 <= a + b:
        print(3)
    else:
        print(4)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if (A + B >= 15) and (B >= 8):
        print(1)
    elif (A + B >= 10) and (B >= 3):
        print(2)
    elif (A + B >= 3):
        print(3)
    else:
        print(4)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A >= 15 and B >= 8:
        print(1)
    elif A >= 10 and B >= 3:
        print(2)
    elif A >= 3 and B >= 0:
        print(3)
    elif A >= 0 and B >= 0:
        print(4)
    else:
        print("Error")

=======
Suggestion 7

def ice_cream_type(a, b):
    if a >= 15 and b >= 8:
        return 1
    elif a >= 10 and b >= 3:
        return 2
    elif a >= 3:
        return 3
    else:
        return 4

=======
Suggestion 8

def main():
    #read input
    a,b = map(int,input().split())
    #process
    if a >= 15 and b >= 8:
        print(1)
    elif a >= 10 and b >= 3:
        print(2)
    elif a >= 3:
        print(3)
    else:
        print(4)
    #output
