def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if i == H - 1 and j == W - 1:
                    pass
                elif i == H - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for a in ans:
        print(*a)
solve()

if __name__ == '__main__':
    solve()