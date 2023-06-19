def solve(H, W, N, AB):
    row = [0] * W
    col = [0] * H
    for i in range(N):
        row[AB[i][1]-1] = i+1
        col[AB[i][0]-1] = i+1
    for i in range(W):
        if row[i] == 0:
            row[i] = N+1
    for i in range(H):
        if col[i] == 0:
            col[i] = N+1
    return row, col

if __name__ == '__main__':
    solve()