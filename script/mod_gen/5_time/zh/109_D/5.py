def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                if a[i][j] % 2 == 1:
                    if j < W-1:
                        a[i][j+1] += 1
                        ans.append([i+1, j+1, i+1, j+2])
                    else:
                        if i < H-1:
                            a[i+1][j] += 1
                            ans.append([i+1, j+1, i+2, j+1])
        else:
            for j in range(W-1, -1, -1):
                if a[i][j] % 2 == 1:
                    if j > 0:
                        a[i][j-1] += 1
                        ans.append([i+1, j+1, i+1, j])
                    else:
                        if i < H-1:
                            a[i+1][j] += 1
                            ans.append([i+1, j+1, i+2, j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    main()