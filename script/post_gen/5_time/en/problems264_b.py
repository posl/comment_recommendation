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
Suggestion 3

def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print('white')
        else:
            print('black')
    else:
        if C % 2 == 0:
            print('black')
        else:
            print('white')

=======
Suggestion 4

def main():
    r, c = map(int, input().split())
    if (r + c) % 2 == 0:
        print('white')
    else:
        print('black')

=======
Suggestion 5

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print('white')
    else:
        print('black')

=======
Suggestion 6

def main():
    r, c = [int(x) for x in input().split()]
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
Suggestion 7

def print_color(r, c):
    if (r + c) % 2 == 0:
        print("black")
    else:
        print("white")
