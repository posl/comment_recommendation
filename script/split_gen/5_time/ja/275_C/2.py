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
