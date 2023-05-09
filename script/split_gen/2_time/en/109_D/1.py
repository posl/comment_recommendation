def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i % 2 == 0 and j != W - 1:
                if A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                    A[i][j + 1] += 1
            elif i % 2 == 0 and j == W - 1:
                if i != H - 1 and A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 2, j + 1))
                    A[i + 1][j] += 1
            elif i % 2 == 1 and j != 0:
                if A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 1, j))
                    A[i][j - 1] += 1
            elif i % 2 == 1 and j == 0:
                if i != H - 1 and A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 2, j + 1))
                    A[i + 1][j] += 1
    print(len(ans))
    for a in ans:
        print(*a)
