Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r, c = map(int, input().split())
    if r % 2 == 0:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
    else:
        if c % 2 == 0:
            print("black")
        else:
            print("white")

=======
Suggestion 2

def main():
    r, c = map(int, input().split())
    if r % 2 == 0:
        if c % 2 == 0:
            print('white')
        else:
            print('black')
    else:
        if c % 2 == 0:
            print('black')
        else:
            print('white')

=======
Suggestion 3

def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print("white")
        else:
            print("black")
    else:
        if C % 2 == 0:
            print("black")
        else:
            print("white")

=======
Suggestion 4

def main():
    r, c = (int(x) for x in input().split())
    if r % 2 == 0:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
    else:
        if c % 2 == 0:
            print("black")
        else:
            print("white")

=======
Suggestion 5

def main():
    R, C = map(int, input().split())
    print("black" if (R + C) % 2 == 0 else "white")

=======
Suggestion 6

def main():
    row, col = map(int, input().split())
    if row <= 8 and col <= 8:
        print("white")
    else:
        print("black")

=======
Suggestion 7

def main():
    # Take input Here and Call solution function
    r,c = map(int,input().strip().split())
    if r%2 == 0 and c%2 == 0:
        print("white")
    elif r%2 == 0 and c%2 != 0:
        print("black")
    elif r%2 != 0 and c%2 == 0:
        print("black")
    elif r%2 != 0 and c%2 != 0:
        print("white")
    return 0
