def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # H, W = 500, 500
    # A = [[9] * W for _ in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2:
                if j + 1 < W:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                    N += 1
                elif i + 1 < H:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))
                    N += 1
    print(N)
    for a in ans:
        print(*a)
