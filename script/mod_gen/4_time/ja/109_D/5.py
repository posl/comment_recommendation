def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i != H - 1:
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
            else:
                if j != W - 1:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i][j + 1] += 1
                        ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

if __name__ == '__main__':
    main()