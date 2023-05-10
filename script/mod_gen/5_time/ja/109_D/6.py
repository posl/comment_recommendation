def solve():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j != w - 1:
                    a[i][j + 1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                elif i != h - 1:
                    a[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
solve()

if __name__ == '__main__':
    solve()