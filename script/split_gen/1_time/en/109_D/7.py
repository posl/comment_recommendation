def main():
    H, W = [int(x) for x in input().split()]
    a = [list(input().split()) for _ in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if int(a[i][j]) % 2 == 1:
                if j < W - 1:
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    N += 1
                elif i < H - 1:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    N += 1
    print(N)
    for i in range(N):
        print(" ".join([str(x) for x in ans[i]]))
