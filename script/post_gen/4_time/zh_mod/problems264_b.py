Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R,C = input().split()
    R = int(R)
    C = int(C)
    if R%2 == 0:
        if C%2 == 0:
            print("w

=======
Suggestion 2

def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print("black")

=======
Suggestion 3

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("whit

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    if (R+C)%2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 5

def main():
    R, C = map(int, input().split())
    if (R+C)%2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 6

def print_color(row, col):
    if row % 2 == 0:
        if col % 2 == 0:
            print("white")
        els

=======
Suggestion 7

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("white")
    else:
        print("blac

=======
Suggestion 8

def get_color(row, col):
    if (row + col) % 2 == 0:
        return 'black'
    else:
        return 'white'

=======
Suggestion 9

def print_color(r, c):
    # 1. 判断奇偶
    if r % 2 == 0:
        # 2. 偶数行
        if c % 2 == 0:
            # 4. 偶数列
