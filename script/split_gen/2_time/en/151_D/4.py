def main():
    H,W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                S[i][j] = 0
            else:
                S[i][j] = -1
    for i in range(H):
        for j in range(W):
            if S[i][j] != -1:
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    S[i][j] = S[i][j-1] + 1
                elif j == 0:
                    S[i][j] = S[i-1][j] + 1
                else:
                    S[i][j] = max(S[i-1][j], S[i][j-1]) + 1
    print(S[-1][-1])
main()
