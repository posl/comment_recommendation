Synthesizing 10/10 solutions

=======
Suggestion 1

def check(fld):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if fld[i][j] == "#":
                cnt += 1
    return cnt

=======
Suggestion 2

def main():
    S = []
    for i in range(9):
        S.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    board = []
    for _ in range(9):
        board.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == "#":
                continue
            for k in range(9):
                if board[k][j] == "#":
                    continue
                if (board[i][j] == "." and board[k][j] == ".") or (board[i][j] == "." and board[i][k] == "."):
                    continue
                if i + k - j < 0 or i + k - j >= 9:
                    continue
                if board[i + k - j][k] == "#":
                    continue
                if board[i + k - j][k] == "." and board[k][j] == "." and board[i][j] == ".":
                    continue
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # input
    S = [input() for _ in range(9)]

    # compute
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                ans += 1
    ans = ans // 4

    # output
    print(ans)

=======
Suggestion 5

def main():
    s = []
    for i in range(9):
        s.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 6

def main():
    s = []
    for i in range(9):
        s.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    # 整数 1 つ
    #N = int(input())
    # 整数複数個
    #A, B = map(int, input().split())
    # 整数複数個（リスト）
    #A = list(map(int, input().split()))
    # 文字列 1 つ
    #S = input()
    # 文字列複数個
    #S = [input() for i in range(N)]
    # 整数 N 個
    #A = [int(input()) for i in range(N)]
    # 整数 N 個（スペース区切り一括入力）
    #A = list(map(int, input().split()))
    # 整数 N 個（改行区切り一括入力）
    #A = [int(input()) for i in range(N)]

    S = [input() for i in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                cnt += 1
    print(cnt)

=======
Suggestion 8

def get_input():
    input_list = []
    for i in range(9):
        input_list.append(input())
    return input_list

=======
Suggestion 9

def main():
    s = []
    for i in range(9):
        s.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                if i - 1 >= 0 and j - 1 >= 0:
                    if s[i - 1][j] == "#" and s[i][j - 1] == "#" and s[i - 1][j - 1] == "#":
                        ans += 1
    print(ans)

=======
Suggestion 10

def main():
    # リストの入力
    S = [input() for i in range(9)]
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                if i + 1 < 9 and j + 1 < 9:
                    if S[i + 1][j] == "#" and S[i][j + 1] == "#" and S[i + 1][j + 1] == "#":
                        count += 1
    print(count)
