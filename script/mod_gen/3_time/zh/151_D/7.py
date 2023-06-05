def maze():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                S[i][j] = 0
            else:
                S[i][j] = -1
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                S[i][j] = 1
                for k in range(1, H):
                    if i + k < H and S[i + k][j] != -1:
                        S[i + k][j] = S[i][j] + 1
                    else:
                        break
                for k in range(1, H):
                    if i - k >= 0 and S[i - k][j] != -1:
                        S[i - k][j] = S[i][j] + 1
                    else:
                        break
                for k in range(1, W):
                    if j + k < W and S[i][j + k] != -1:
                        S[i][j + k] = S[i][j] + 1
                    else:
                        break
                for k in range(1, W):
                    if j - k >= 0 and S[i][j - k] != -1:
                        S[i][j - k] = S[i][j] + 1
                    else:
                        break
                ans = max(ans, S[i][j])
    print(ans)
maze()
