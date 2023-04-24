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
main()

=======
Suggestion 2

def main():
    r, c = map(int, input().split())
    if r%2 == 0:
        if c%2 == 0:
            print("white")
        else:
            print("black")
    else:
        if c%2 == 0:
            print("black")
        else:
            print("white")

=======
Suggestion 3

def main():
    r, c = map(int, input().split())
    if r%2 == 0:
        if c%2 == 0:
            print('white')
        else:
            print('black')
    else:
        if c%2 == 0:
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
    r, c = map(int, input().split())
    if r % 2 == 0 and c % 2 == 0:
        print("white")
    elif r % 2 == 0 and c % 2 != 0:
        print("black")
    elif r % 2 != 0 and c % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 6

def get_color(row, col):
    if row % 2 == 0:
        if col % 2 == 0:
            return 'white'
        else:
            return 'black'
    else:
        if col % 2 == 0:
            return 'black'
        else:
            return 'white'

=======
Suggestion 7

def main():
    R, C = map(int, input().split())
    if (R+C)%2 == 0:
        print('white')
    else:
        print('black')

=======
Suggestion 8

def main():
    r, c = map(int, input().split())
    print("black" if (r + c) % 2 == 0 else "white")

=======
Suggestion 9

def main():
    r,c = map(int, input().split())
    if r%2 != 0:
        if c%2 != 0:
            print('black')
        else:
            print('white')
    else:
        if c%2 != 0:
            print('white')
        else:
            print('black')
