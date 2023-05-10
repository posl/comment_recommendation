Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r,c = map(int, input().split())
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
Suggestion 2

def main():
    r,c = map(int,input().split())
    if r > 0 and r <= 15 and c > 0 and c <= 15:
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
Suggestion 3

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
Suggestion 4

def main():
    R, C = map(int, input().split())
    if R%2 == 0:
        if C%2 == 0:
            print("white")
        else:
            print("black")
    else:
        if C%2 == 0:
            print("black")
        else:
            print("white")

=======
Suggestion 5

def main():
    R, C = map(int, input().split())
    if R % 2 == 0 and C % 2 == 0:
        print("white")
    elif R % 2 == 0 and C % 2 != 0:
        print("black")
    elif R % 2 != 0 and C % 2 == 0:
        print("black")
    else:
        print("white")
