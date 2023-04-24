Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
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
Suggestion 4

def main():
    R, C = map(int, input().split())
    if R % 2 == 1 and C % 2 == 1:
        print('black')
    else:
        print('white')

=======
Suggestion 5

def main():
    r, c = map(int, input().split())
    if (r * c) % 2 == 0:
        print('white')
    else:
        print('black')

main()

=======
Suggestion 6

def main():
    R, C = map(int, input().split())
    grid = []
    for i in range(15):
        grid.append([])
        for j in range(15):
            if (i + j) % 2 == 0:
                grid[i].append("black")
            else:
                grid[i].append("white")
    print(grid[R - 1][C - 1])

=======
Suggestion 7

def main():
    #input
    R,C = map(int, input().split())

    #output
    if (R%2 == 1 and C%2 == 1) or (R%2 == 0 and C%2 == 0):
        print('black')
    else:
        print('white')

=======
Suggestion 8

def main():
    # 標準入力から、R(行), C(列)を取得
    R, C = map(int, input().split())
    # 図のグリッドにおいて上から R 行目、左から C 列目のマスが黒色の場合は black と、白色の場合は white と出力せよ。
    if (R * C) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 9

def main():
    # R行目、C列目のマスの色を出力する
    R, C = map(int, input().split())
    # グリッドの初期化
    grid = [['white' for i in range(15)] for j in range(15)]
    # グリッドの塗りつぶし
    for i in range(15):
        for j in range(15):
            if (i + j) % 2 == 0:
                grid[i][j] = 'black'
    # 結果の出力
    print(grid[R - 1][C - 1])

=======
Suggestion 10

def main():
    #入力
    R, C = map(int, input().split())
    #黒色のマスの座標をタプルでリスト化
    black = [(1,1),(1,4),(1,7),(1,10),(1,13),(1,16),(4,1),(4,4),(4,7),(4,10),(4,13),(4,16),(7,1),(7,4),(7,7),(7,10),(7,13),(7,16),(10,1),(10,4),(10,7),(10,10),(10,13),(10,16),(13,1),(13,4),(13,7),(13,10),(13,13),(13,16),(16,1),(16,4),(16,7),(16,10),(16,13),(16,16)]
    #黒色のマスの座標が入力された場合はblackを出力
    if (R, C) in black:
        print("black")
    #白色のマスの座標が入力された場合はwhiteを出力
    else:
        print("white")
