def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    N += 1
                elif i < H - 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    N += 1
    print(N)
    for i in range(N):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])
main()
