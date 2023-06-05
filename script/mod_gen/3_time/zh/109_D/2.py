def solve():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                if j == w - 1:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append((i + 1, j + 1, i + 2, j + 1))
                else:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i][j + 1] += 1
                        ans.append((i + 1, j + 1, i + 1, j + 2))
            else:
                if j == 0:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append((i + 1, j + 1, i + 2, j + 1))
                else:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i][j - 1] += 1
                        ans.append((i + 1, j + 1, i + 1, j))
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    solve()