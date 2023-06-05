def solution(h, w, board):
    x = []
    y = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'o':
                x.append(i)
                y.append(j)
    res = 1e9
    for i in range(h):
        for j in range(w):
            if board[i][j] == '-':
                continue
            tmp = 0
            for k in range(len(x)):
                tmp += abs(x[k] - i) + abs(y[k] - j)
            res = min(res, tmp)
    return res

if __name__ == '__main__':
    solution()