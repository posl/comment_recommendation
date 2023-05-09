def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #縦方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(N):
        for j in range(N-5):
            if S[i][j] == '#' and S[i][j+1] == '#' and S[i][j+2] == '#' and S[i][j+3] == '#' and S[i][j+4] == '#' and S[i][j+5] == '#':
                print('Yes')
                return
    #横方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(N-5):
        for j in range(N):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i+2][j] == '#' and S[i+3][j] == '#' and S[i+4][j] == '#' and S[i+5][j] == '#':
                print('Yes')
                return
    #右下方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == '#' and S[i+1][j+1] == '#' and S[i+2][j+2] == '#' and S[i+3][j+3] == '#' and S[i+4][j+4] == '#' and S[i+5][j+5] == '#':
                print('Yes')
                return
    #左下方向に黒く塗られたマスが6つ以上連続するか判定
    for i in range(5,N):
        for j in range(N-5):
            if S[i][j] == '#' and S[i-1][j+1] == '#' and S[i-2][j+2] == '#' and S[i-3][j+3] == '#' and S[i-4][j+4] == '#' and S[i-5][j+5] == '#':
                print('Yes')

if __name__ == '__main__':
    main()