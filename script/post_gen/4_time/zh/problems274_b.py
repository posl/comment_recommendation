Synthesizing 10/10 solutions

=======
Suggestion 1

def problems274_b():
    return None

=======
Suggestion 2

def main():
    h,w = map(int, input().split())
    grid = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                print(j)
                break
        else:
            print(w)
main()

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    for i in range(H):
        print(sum([1 if C[i][j] == "#" else 0 for j in range(W)]))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[i][j] = 1
    for i in range(W):
        for j in range(1, H):
            if X[j][i] == 1:
                X[j][i] = X[j-1][i] + 1
    for i in range(H):
        print(*X[i])

=======
Suggestion 5

def problem274_b():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    for j in range(w):
        count = 0
        for i in range(h):
            if c[i][j] == '#':
                count += 1
        print(count, end=' ')
    print()

=======
Suggestion 6

def problems274_b():
    pass

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] = 1
    print(*X)

=======
Suggestion 8

def find_num_of_boxes(H, W, C):
    # print(H, W, C)
    X = [[0 for i in range(W)] for i in range(H)]
    # print(X)
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[i][j] = 1
    # print(X)

    for j in range(W):
        for i in range(1, H):
            if X[i][j] == 1:
                X[0][j] += 1
    # print(X)

    for j in range(W):
        for i in range(1, H):
            if X[H - i - 1][j] == 1:
                X[H - 1][j] += 1
    # print(X)

    for i in range(H):
        for j in range(1, W):
            if X[i][j] == 1:
                X[i][0] += 1
    # print(X)

    for i in range(H):
        for j in range(1, W):
            if X[i][W - j - 1] == 1:
                X[i][W - 1] += 1
    # print(X)

    for i in range(H):
        for j in range(W):
            if X[i][j] == 4:
                X[i][j] = 0
    # print(X)

    for i in range(H):
        for j in range(W):
            if X[i][j] == 1:
                X[i][j] = 0
    # print(X)

    for i in range(H):
        for j in range(W):
            if X[i][j] == 2:
                X[i][j] = 1
    # print(X)

    for i in range(H):
        for j in range(W):
            if X[i][j] == 3:
                X[i][j] = 1
    # print(X)

    for i in range(H):
        for j in range(W):
            if X[i][j] == 0:
                X[i][j] = '.'
    # print(X)

    for i in range(H):
        for j in range(W):
            if X[i][j] == 1:
                X[i][j] =

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]

    for i in range(H):
        count = 0
        for j in range(W):
            if C[i][j] == '#':
                count += 1
        print(count)

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    board = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        board[i] = list(input())
    for i in range(H):
        for j in range(W):
            if board[i][j] == "#":
                board[i][j] = 1
            else:
                board[i][j] = 0
    ans = [0 for _ in range(W)]
    for j in range(W):
        for i in range(H):
            ans[j] += board[i][j]
    return ans
