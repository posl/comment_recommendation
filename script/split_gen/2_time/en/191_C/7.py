def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #外枠を白に塗りつぶす
    for i in range(H):
        S[i][0] = '.'
        S[i][W-1] = '.'
    for j in range(W):
        S[0][j] = '.'
        S[H-1][j] = '.'
    #print(S)
    #白のマスを見つける
    white = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                white.append((i, j))
    #print(white)
    #白マスから黒マスにたどり着くまでを探索する
    for i, j in white:
        #print(i, j)
        if i-1 >= 0 and S[i-1][j] == '#':
            print(4)
            return
        if i+1 < H and S[i+1][j] == '#':
            print(4)
            return
        if j-1 >= 0 and S[i][j-1] == '#':
            print(4)
            return
        if j+1 < W and S[i][j+1] == '#':
            print(4)
            return
