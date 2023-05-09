def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                break
            if A[i][j] % 2 == 1:
                N += 1
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(N)
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()