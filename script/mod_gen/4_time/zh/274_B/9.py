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

if __name__ == '__main__':
    solve()