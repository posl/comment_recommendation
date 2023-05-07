def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j + 1 < W:
                    ans.append((i, j, i, j + 1))
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                elif i + 1 < H:
                    ans.append((i, j, i + 1, j))
                    A[i][j] -= 1
                    A[i + 1][j] += 1
    print(len(ans))
    for i, j, k, l in ans:
        print(i + 1, j + 1, k + 1, l + 1)
