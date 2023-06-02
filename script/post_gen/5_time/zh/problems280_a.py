Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 2

def count_chessboard(H, W, S):
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    return count

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    #读取行数和列数
    line = input().split()
    row = int(line[0])
    column = int(line[1])
    #读取棋盘状态，用二维数组存储
    chessboard = [[0 for i in range(column)] for j in range(row)]
    for i in range(row):
        line = input()
        for j in range(column):
            if line[j] == '#':
                chessboard[i][j] = 1
    #计算棋盘上的棋子数
    sum = 0
    for i in range(row):
        for j in range(column):
            sum += chessboard[i][j]
    print(sum)

=======
Suggestion 8

def count_chess():
    h,w = input().split()
    h = int(h)
    w = int(w)
    count = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                count += 1
    return count

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)
