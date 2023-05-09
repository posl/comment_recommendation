def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for k in range(i, H):
                for l in range(j, W):
                    if S[k][l] == "#":
                        continue
                    ans = max(ans, abs(i-k) + abs(j-l))
    print(ans)
