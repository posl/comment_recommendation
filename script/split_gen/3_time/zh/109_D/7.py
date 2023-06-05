def solve(h, w, a):
    ans = []
    for i in range(h):
        if i % 2 == 0:
            for j in range(w - 1):
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
            if i != h - 1 and a[i][w - 1] % 2 == 1:
                a[i][w - 1] -= 1
                a[i + 1][w - 1] += 1
                ans.append([i + 1, w, i + 2, w])
        else:
            for j in range(w - 1, 0, -1):
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i][j - 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j])
            if i != h - 1 and a[i][0] % 2 == 1:
                a[i][0] -= 1
                a[i + 1][0] += 1
                ans.append([i + 1, 1, i + 2, 1])
    print(len(ans))
    for i in ans:
        print(*i)
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
solve(h, w, a)
