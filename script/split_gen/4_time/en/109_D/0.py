def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                continue
            if j == W - 1 and i == H - 1:
                break
            if j == W - 1:
                A[i + 1][j] += 1
                ans.append([i + 1, j + 1, i + 2, j + 1])
            else:
                A[i][j + 1] += 1
                ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for a in ans:
        print(' '.join(map(str, a)))
