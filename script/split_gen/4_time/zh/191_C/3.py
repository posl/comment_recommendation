def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == "#" or S[i+1][j] == "#" or S[i][j+1] == "#" or S[i+1][j+1] == "#":
                ans += 1
    print(ans)
