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
    r,c = map(int,input().split())
    if r % 2 == 0:
        if c % 2 == 0:
            print("black")
        else:
            print("white")
    else:
        if c % 2 == 0:
            print("white")
        else:
            print("black")

=======
Suggestion 4

def main():
    r,c = map(int, input().split())
    if r%2 == 1:
        if c%2 == 1:
            print("black")
        else:
            print("white")
    else:
        if c%2 == 1:
            print("white")
        else:
            print("black")

=======
Suggestion 5

def main():
    r,c = map(int,input().split())
    if r%2 == 0 and c%2 == 0:
        print('white')
    elif r%2 == 0 and c%2 == 1:
        print('black')
    elif r%2 == 1 and c%2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 6

def main():
    r,c = map(int,input().split())
    if 1 <= r and r <= 15 and 1 <= c and c <= 15:
        if r % 2 == 0 and c % 2 == 0:
            print("white")
        elif r % 2 == 0 and c % 2 == 1:
            print("black")
        elif r % 2 == 1 and c % 2 == 0:
            print("black")
        elif r % 2 == 1 and c % 2 == 1:
            print("white")

=======
Suggestion 7

def main():
    # 標準入力から R, C を取得する
    R, C = map(int, input().split())
    # R, C について、black と white を出力する
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
