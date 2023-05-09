def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if S[i][j] == S[k][l] == ".":
                        ans = max(ans, abs(i-k)+abs(j-l))
    print(ans)
