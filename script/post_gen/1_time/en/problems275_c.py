Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = [input() for i in range(9)]
    ans = 0
    for i in range(8):
        for j in range(8):
            if S[i][j] == S[i][j+1] == S[i+1][j] == S[i+1][j+1] == "#":
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i > 0 and j > 0:
                    if S[i - 1][j] == '#' and S[i][j - 1] == '#' and S[i - 1][j - 1] == '#':
                        ans += 1
                if i > 0 and j < 8:
                    if S[i - 1][j] == '#' and S[i][j + 1] == '#' and S[i - 1][j + 1] == '#':
                        ans += 1
                if i < 8 and j > 0:
                    if S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i + 1][j - 1] == '#':
                        ans += 1
                if i < 8 and j < 8:
                    if S[i + 1][j] == '#' and S[i][j + 1] == '#' and S[i + 1][j + 1] == '#':
                        ans += 1
    print(ans // 4)

=======
Suggestion 3

def main():
    S = []
    for _ in range(9):
        S.append(input())
    ans = 0
    for i in range(8):
        for j in range(8):
            if S[i][j] == S[i][j+1] == S[i+1][j] == S[i+1][j+1] == '#':
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    board = []
    for i in range(9):
        board.append(input())
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#' and board[i][j+1] == '#' and board[i+1][j] == '#' and board[i+1][j+1] == '#':
                count += 1
    print(count)

=======
Suggestion 5

def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(8):
        for j in range(8):
            if S[i][j] == '#' and S[i + 1][j] == '#' and S[i][j + 1] == '#' and S[i + 1][j + 1] == '#':
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(8):
        for j in range(8):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if S[i+k][j+l] == "#":
                        cnt += 1
            if cnt == 4:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == ".":
                continue
            if i + 2 < 9 and j + 2 < 9:
                if S[i][j] == "#" and S[i][j + 1] == "#" and S[i][j + 2] == "#" and S[i + 1][j] == "#" and S[i + 1][j + 2] == "#" and S[i + 2][j] == "#" and S[i + 2][j + 1] == "#" and S[i + 2][j + 2] == "#":
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    S = []
    for i in range(9):
        S.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if i+1<9 and j+1<9 and S[i][j]=="#" and S[i+1][j]=="#" and S[i][j+1]=="#" and S[i+1][j+1]=="#":
                ans += 1
    print(ans)
    return

=======
Suggestion 9

def main():
    S = [input() for _ in range(9)]

    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                for x in range(9):
                    for y in range(9):
                        if S[x][y] == '#':
                            for z in range(9):
                                for w in range(9):
                                    if S[z][w] == '#':
                                        for a in range(9):
                                            for b in range(9):
                                                if S[a][b] == '#':
                                                    if i == x == z == a and j < y < w < b:
                                                        ans += 1
                                                    if i == x == a == z and j < w < y < b:
                                                        ans += 1
                                                    if i == z == a == x and j < y < b < w:
                                                        ans += 1
                                                    if i == z == x == a and j < b < y < w:
                                                        ans += 1
                                                    if j == y == w == b and i < x < z < a:
                                                        ans += 1
                                                    if j == y == b == w and i < z < x < a:
                                                        ans += 1
                                                    if j == w == b == y and i < x < a < z:
                                                        ans += 1
                                                    if j == w == y == b and i < a < x < z:
                                                        ans += 1
                                                    if i == x == z == a and j < y < w < b:
                                                        ans += 1
                                                    if i == x == a == z and j < w < y < b:
                                                        ans += 1
                                                    if i == z == a == x and j < y < b < w:
                                                        ans += 1
                                                    if i == z == x == a and j < b < y < w:
                                                        ans += 1
                                                    if j == y == w == b and i < x < z < a:
                                                        ans += 1
                                                    if j == y == b == w and i < z < x < a:
                                                        ans += 1
                                                    if j == w == b == y and i < x < a < z:
                                                        ans += 1
                                                    if j == w == y == b and i < a < x

=======
Suggestion 10

def main():
    #input
    S = []
    for i in range(9):
        S.append(input())
    #solve
    ans = 0
    for i in range(7):
        for j in range(7):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i][j+1] == '#' and S[i+1][j+1] == '#':
                ans += 1
    #output
    print(ans)
