Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    if R % 2 == 1:
        if C % 2 == 1:
            print('black')
        else:
            print('white')
    else:
        if C % 2 == 1:
            print('white')
        else:
            print('black')

=======
Suggestion 2

def main():
    r, c = map(int, input().split())
    if (r + c) % 2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 3

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    if R % 2 == 0 and C % 2 == 0:
        print('black')
    elif R % 2 == 1 and C % 2 == 1:
        print('black')
    else:
        print('white')

=======
Suggestion 5

def main():
    r, c = map(int, input().split())
    if (r * c) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 6

def main():
    R, C = map(int, input().split())
    if R % 2 == 0 and C % 2 == 0:
        print('black')
    elif R % 2 == 0 and C % 2 != 0:
        print('white')
    elif R % 2 != 0 and C % 2 == 0:
        print('white')
    elif R % 2 != 0 and C % 2 != 0:
        print('black')

=======
Suggestion 7

def main():
    r,c = map(int, input().split())
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

main()

=======
Suggestion 8

def main():
    R, C = map(int, input().split())
    if (R*C)%2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 9

def main():
    r, c = map(int, input().split())
    print("black" if (r + c) % 2 == 0 else "white")
