def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans += 1
    if ans == H*W:
        print(ans-1)
    else:
        print(ans)
