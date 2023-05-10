def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]
    # print(S)
    # print(T)
    if S == T:
        print('Yes')
        return
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                # print(i,j)
                if 0 <= i-1 and 0 <= j-1 and S[i-1][j-1] == '#':
                    S[i-1][j-1] = '.'
                if 0 <= i-1 and S[i-1][j] == '#':
                    S[i-1][j] = '.'
                if 0 <= i-1 and j+1 <= W-1 and S[i-1][j+1] == '#':
                    S[i-1][j+1] = '.'
                if 0 <= j-1 and S[i][j-1] == '#':
                    S[i][j-1] = '.'
                if j+1 <= W-1 and S[i][j+1] == '#':
                    S[i][j+1] = '.'
                if i+1 <= H-1 and 0 <= j-1 and S[i+1][j-1] == '#':
                    S[i+1][j-1] = '.'
                if i+1 <= H-1 and S[i+1][j] == '#':
                    S[i+1][j] = '.'
                if i+1 <= H-1 and j+1 <= W-1 and S[i+1][j+1] == '#':
                    S[i+1][j+1] = '.'
    if S == T:
        print('Yes')
    else:
        print('No')
