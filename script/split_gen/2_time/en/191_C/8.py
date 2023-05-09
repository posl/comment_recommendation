def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    # まず、白の部分を塗りつぶす
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i][j] = 'x'
    # 左上から右下への経路を見つける
    # まず、左上から右に行き、下に行く
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if j == 0:
                if S[i-1][j] == '#':
                    S[i][j] = '#'
                continue
            if S[i][j-1] == '#':
                S[i][j] = '#'
    # 次に、左下から上に行き、右に行く
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                continue
            if i == H-1:
                if S[i][j+1] == '#':
                    S[i][j] = '#'
                continue
            if j == W-1:
                if S[i+1][j] == '#':
                    S[i][j] = '#'
                continue
            if S[i][j+1] == '#':
                S[i][j] = '#'
            if S[i+1][j] == '#':
                S[i][j] = '#'
    # まず、左上から右下への経路を見つける
    # まず、左上から右に行き、下に行く
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if j == 0:
                if S[i-1][j] == '#':
                    S[i][j] = '#'
                continue
            if S[i][j-1] == '#':
                S[i][j] = '#
