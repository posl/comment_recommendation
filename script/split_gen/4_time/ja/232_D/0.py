def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                continue
            cnt = 1
            for k in range(1, H+W):
                if i+k < H and j+k < W:
                    if C[i+k][j] == "#" or C[i][j+k] == "#":
                        break
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    print(ans)
