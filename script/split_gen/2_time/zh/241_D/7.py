def main():
    N = int(input())
    S = [input() for i in range(N)]
    # print(N)
    # print(S)
    # 1. 6连续黑色方格是否存在
    # 2. 6连续黑色方格是否存在
    # 3. 6连续黑色方格是否存在
    # 4. 6连续黑色方格是否存在
    # 5. 6连续黑色方格是否存在
    # 6. 6连续黑色方格是否存在
    # 1. 6连续黑色方格是否存在
    for i in range(N):
        for j in range(N-5):
            if S[i][j] == S[i][j+1] == S[i][j+2] == S[i][j+3] == S[i][j+4] == S[i][j+5] == '#':
                print('Yes')
                exit()
    # 2. 6连续黑色方格是否存在
    for i in range(N-5):
        for j in range(N):
            if S[i][j] == S[i+1][j] == S[i+2][j] == S[i+3][j] == S[i+4][j] == S[i+5][j] == '#':
                print('Yes')
                exit()
    # 3. 6连续黑色方格是否存在
    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == S[i+1][j+1] == S[i+2][j+2] == S[i+3][j+3] == S[i+4][j+4] == S[i+5][j+5] == '#':
                print('Yes')
                exit()
    # 4. 6连续黑色方格是否存在
    for i in range(N-5):
        for j in range(5, N):
            if S[i][j] == S[i+1][j-1] == S[i+2][j-2] == S[i+3][j-3] == S[i+4][j-4]
