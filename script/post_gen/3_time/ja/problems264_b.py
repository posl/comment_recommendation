Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    if (R % 2 == 1 and C % 2 == 1) or (R % 2 == 0 and C % 2 == 0):
        print('black')
    else:
        print('white')

=======
Suggestion 2

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 3

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 4

def main():
    r, c = map(int, input().split())
    if ((r + c) % 2 == 0):
        print("black")
    else:
        print("white")

=======
Suggestion 5

def main():
    #入力
    R, C = map(int, input().split())

    #出力
    if (R + C) % 2 == 0:
        print('black')
    else:
        print('white')

=======
Suggestion 6

def main():
    R, C = map(int, input().split())
    if (R*C)%2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 7

def main():
    # R C
    # 1 ≦ R, C ≦ 15
    # R, C は整数
    R, C = map(int, input().split())

    # 黒白を判定
    if (R % 2 == 0 and C % 2 == 0) or (R % 2 == 1 and C % 2 == 1):
        print("black")
    else:
        print("white")

=======
Suggestion 8

def main():
    R, C = map(int, input().split())
    #黒白のグリッドを作成
    grid = [["black", "white"] * 8, ["white", "black"] * 8] * 8
    #黒白のグリッドのR行目C列目を出力
    print(grid[R-1][C-1])

=======
Suggestion 9

def main():
    # R:行数、C:列数
    R, C = map(int, input().split())
    # グリッドの塗り分け
    if (R * C) % 2 == 0:
        print("white")
    else:
        print("black")
