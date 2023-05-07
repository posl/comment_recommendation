def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # print(N)
    # print(S)
    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == ".":
                if S[i][j+1] == "." and S[i][j+2] == "." and S[i][j+3] == "." and S[i][j+4] == "." and S[i][j+5] == ".":
                    print("Yes")
                    return
                if S[i+1][j] == "." and S[i+2][j] == "." and S[i+3][j] == "." and S[i+4][j] == "." and S[i+5][j] == ".":
                    print("Yes")
                    return
                if S[i+1][j+1] == "." and S[i+2][j+2] == "." and S[i+3][j+3] == "." and S[i+4][j+4] == "." and S[i+5][j+5] == ".":
                    print("Yes")
                    return
                if S[i+1][j-1] == "." and S[i+2][j-2] == "." and S[i+3][j-3] == "." and S[i+4][j-4] == "." and S[i+5][j-5] == ".":
                    print("Yes")
                    return
    print("No")
