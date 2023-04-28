Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 標準入力から H, W を取得する
    H, W = map(int, input().split())
    # 標準入力から C_{i,j} を取得する
    C = [input() for i in range(H)]
    # X を初期化する
    X = [0] * W
    # X を求める
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    # X を出力する
    print(*X)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]

    x = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == '#':
                x[i] += 1

    print(' '.join(map(str, x)))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    ans = [0]*w
    for i in range(w):
        for j in range(h):
            if c[j][i] == "#":
                ans[i] += 1
    print(*ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    
    for i in range(H):
        count = 0
        for j in range(W):
            if grid[i][j] == '#':
                count += 1
        print(count, end=' ')
    print()

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    ans = [0] * w
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                ans[j] += 1
    print(*ans)

=======
Suggestion 6

def resolve():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    X = [0] * W

    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                X[j] += 1

    for i in range(W):
        print(X[i], end=" ")
    print()

=======
Suggestion 7

def main():
    # 標準入力から1行取得
    line = input()
    # 空白で分割して2つの整数として扱う
    H, W = map(int, line.split())
    # 標準入力からH行取得してリストに格納
    S = [input() for i in range(H)]
    # 各列について、#の数を数える
    ans = [0] * W
    for i in range(W):
        for j in range(H):
            if S[j][i] == '#':
                ans[i] += 1
    # 結果を出力
    print(*ans)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    #print(h, w)
    grid = []
    for i in range(h):
        grid.append(input())
    #print(grid)
    for i in range(w):
        count = 0
        for j in range(h):
            #print(grid[j][i])
            if grid[j][i] == "#":
                count += 1
        print(count)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    # print(grid)
    ans = []
    for i in range(W):
        tmp = 0
        for j in range(H):
            if grid[j][i] == "#":
                tmp += 1
        ans.append(tmp)
    print(" ".join(map(str, ans)))

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    ans = []
    for i in range(H):
        ans.append(input().count("#"))
    print(*ans)
