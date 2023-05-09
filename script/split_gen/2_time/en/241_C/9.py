def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    # 2x2の黒マスが存在するか
    for i in range(N - 1):
        for j in range(N - 1):
            if S[i][j] == S[i + 1][j] == S[i][j + 1] == S[i + 1][j + 1] == "#":
                print("Yes")
                return
    # 3x3の白マスが存在するか
    for i in range(N - 2):
        for j in range(N - 2):
            if S[i][j] == S[i + 1][j] == S[i + 2][j] == S[i][j + 1] == S[i + 1][j + 1] == S[i + 2][j + 1] == S[i][j + 2] == S[i + 1][j + 2] == S[i + 2][j + 2] == ".":
                print("Yes")
                return
    # 4x4の白マスが存在するか
    for i in range(N - 3):
        for j in range(N - 3):
            if S[i][j] == S[i + 1][j] == S[i + 2][j] == S[i + 3][j] == S[i][j + 1] == S[i + 1][j + 1] == S[i + 2][j + 1] == S[i + 3][j + 1] == S[i][j + 2] == S[i + 1][j + 2] == S[i + 2][j + 2] == S[i + 3][j + 2] == S[i][j + 3] == S[i + 1][j + 3] == S[i + 2][j + 3] == S[i + 3][j + 3] == ".":
                print("Yes")
                return
    print("No")
