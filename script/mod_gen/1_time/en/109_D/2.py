def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 0:
                continue
            if j + 1 < W:
                ans.append((i + 1, j + 1, i + 1, j + 2))
                a[i][j + 1] += 1
            elif i + 1 < H:
                ans.append((i + 1, j + 1, i + 2, j + 1))
                a[i + 1][j] += 1
    print(len(ans))
    for i in ans:
        print(*i)

if __name__ == '__main__':
    main()