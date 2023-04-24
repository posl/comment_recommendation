Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 2

def get_input_data():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    return h, w, r, c

=======
Suggestion 3

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(4 if (R==1 or R==H) and (C==1 or C==W) else 3 if (R==1 or R==H) or (C==1 or C==W) else 2)

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-1)*w + (w-1)*h - (h-1)*(w-1))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())

    print(0)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(H * W - (R * W + C * H - R * C))

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(count(h, w, r, c))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(3)
    return

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    print("Hello World!")

=======
Suggestion 10

def main():
    # 2次元配列を作成
    # 1次元目がH、2次元目がW
    h, w = map(int, input().split())
    r, c = map(int, input().split())

    # 1次元目の長さがhで、2次元目の長さがwの2次元配列を作成
    # 1次元目の長さがhで、2次元目の長さがwの2次元配列を作成
    # array = [[0 for j in range(w)] for i in range(h)]
    array = [[0]*w for i in range(h)]

    # 配列に値を入れる
    for i in range(h):
        for j in range(w):
            array[i][j] = abs(r-1-i) + abs(c-1-j)

    # 配列を出力する
    # for i in range(h):
    #     print(array[i])
    print(array[r-1][c-1])
