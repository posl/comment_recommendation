def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    # 6 or more consecutive squares painted black aligned horizontally
    for i in range(N):
        for j in range(N - 5):
            if S[i][j] == S[i][j + 1] == S[i][j + 2] == S[i][j + 3] == S[i][j + 4] == S[i][j + 5] == ".":
                print("Yes")
                exit()
    # 6 or more consecutive squares painted black aligned vertically
    for i in range(N - 5):
        for j in range(N):
            if S[i][j] == S[i + 1][j] == S[i + 2][j] == S[i + 3][j] == S[i + 4][j] == S[i + 5][j] == ".":
                print("Yes")
                exit()
    # 6 or more consecutive squares painted black aligned diagonally
    for i in range(N - 5):
        for j in range(N - 5):
            if S[i][j] == S[i + 1][j + 1] == S[i + 2][j + 2] == S[i + 3][j + 3] == S[i + 4][j + 4] == S[i + 5][j + 5] == ".":
                print("Yes")
                exit()
            if S[i][j + 5] == S[i + 1][j + 4] == S[i + 2][j + 3] == S[i + 3][j + 2] == S[i + 4][j + 1] == S[i + 5][j] == ".":
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()