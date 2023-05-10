def check(N, S):
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                if i <= N - 6:
                    if S[i + 1][j] == "#" and S[i + 2][j] == "#" and S[i + 3][j] == "#" and S[i + 4][j] == "#" and S[i + 5][j] == "#":
                        return True
                if j <= N - 6:
                    if S[i][j + 1] == "#" and S[i][j + 2] == "#" and S[i][j + 3] == "#" and S[i][j + 4] == "#" and S[i][j + 5] == "#":
                        return True
                if i <= N - 6 and j <= N - 6:
                    if S[i + 1][j + 1] == "#" and S[i + 2][j + 2] == "#" and S[i + 3][j + 3] == "#" and S[i + 4][j + 4] == "#" and S[i + 5][j + 5] == "#":
                        return True
                if i <= N - 6 and j >= 5:
                    if S[i + 1][j - 1] == "#" and S[i + 2][j - 2] == "#" and S[i + 3][j - 3] == "#" and S[i + 4][j - 4] == "#" and S[i + 5][j - 5] == "#":
                        return True
    return False
N = int(input())
S = [input() for _ in range(N)]
