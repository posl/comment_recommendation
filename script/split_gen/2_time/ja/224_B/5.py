def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            for k in range(i + 1, H):
                for l in range(j + 1, W):
                    if a[i][j] + a[k][l] > a[k][j] + a[i][l]:
                        print('No')
                        return
    print('Yes')
