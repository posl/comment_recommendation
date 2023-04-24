Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    if (R % 2 == 0 and C % 2 == 0) or (R % 2 == 1 and C % 2 == 1):
        print("black")
    else:
        print("white")

=======
Suggestion 2

def main():
    r, c = map(int, input().split())
    if (r + c) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 3

def main():
    r, c = map(int, input().split())
    if (r + c) % 2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 5

def main():
    R, C = map(int, input().split())
    if (R * C) % 2 == 0:
        print('white')
    else:
        print('black')

=======
Suggestion 6

def main():
    #入力
    R, C = map(int, input().split())
    #出力
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 7

def main():
    R,C = map(int,input().split())
    if (R*C)%2 == 0:
        print("white")
    else:
        print("black")

=======
Suggestion 8

def main():
    R, C = map(int,input().split())
    black = [2, 4, 6, 8, 10, 12, 14]
    white = [1, 3, 5, 7, 9, 11, 13]
    if R in black:
        if C in black:
            print("black")
        else:
            print("white")
    else:
        if C in black:
            print("white")
        else:
            print("black")

=======
Suggestion 9

def main():
    # R:行 C:列
    R, C = map(int, input().split())
    # リストの初期化
    grid = []
    # リストに入力を追加
    for r in range(15):
        grid.append(list(input()))
    # リストの表示
    for r in range(15):
        print(grid[r])
    # リストの表示
    for r in range(15):
        print(grid[r][C-1], end="")
    print()
    # リストの表示
    for r in range(15):
        print(grid[R-1][r], end="")
    print()

    # 1行目とC列目の奇数偶数を調べる
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")
