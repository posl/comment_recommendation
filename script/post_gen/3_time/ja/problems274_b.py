Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == "#":
                X[j] += 1
    print(*X)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for j in range(w):
        x = 0
        for i in range(h):
            if c[i][j] == '#':
                x += 1
        print(x, end=' ')
    print()

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    X = [0 for _ in range(W)]
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    X = [0] * W
    for i in range(W):
        for j in range(H):
            if C[j][i] == '#':
                X[i] += 1
    print(" ".join(map(str, X)))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(w):
        print(sum(1 for j in range(h) if c[j][i] == '#'), end=' ')
    print()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    #print(C)
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == "#":
                X[j] += 1
    print(*X)

=======
Suggestion 7

def main():
    # 入力
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    # 出力
    for j in range(W):
        print(sum(1 for i in range(H) if C[i][j] == '#'), end=' ')
    print()

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    #print(h, w)
    c = []
    for i in range(h):
        c.append(input())
    #print(c)
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == "#":
                x += 1
        print(x, end = " ")
    print()

=======
Suggestion 9

def main():
    #入力
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    #print(H, W)
    #print(C)
    #初期化
    X = [0 for i in range(W)]
    #print(X)
    #計算
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[j] += 1
    #出力
    print(*X)

=======
Suggestion 10

def main():
    #入力
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    #print(H, W, C)
    #処理
    #X_j = j 列目に置かれている箱の個数
    X = [0] * W
    for i in range(W):
        for j in range(H):
            if C[j][i] == '#':
                X[i] += 1
    #出力
    print(*X)
