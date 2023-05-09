def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                if i == 0 or i == H-1 or j == 0 or j == W-1:
                    print(4)
                    exit()
                if i > 0 and S[i-1][j] == ".":
                    ans += 1
                if i < H-1 and S[i+1][j] == ".":
                    ans += 1
                if j > 0 and S[i][j-1] == ".":
                    ans += 1
                if j < W-1 and S[i][j+1] == ".":
                    ans += 1
    print(ans)
