def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 0:
                continue
            if j + 1 < W:
                ans.append((i, j, i, j + 1))
                a[i][j] -= 1
                a[i][j + 1] += 1
            elif i + 1 < H:
                ans.append((i, j, i + 1, j))
                a[i][j] -= 1
                a[i + 1][j] += 1
    print(len(ans))
    for y, x, y2, x2 in ans:
        print(y + 1, x + 1, y2 + 1, x2 + 1)
