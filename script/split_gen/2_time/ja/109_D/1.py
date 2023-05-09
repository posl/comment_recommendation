def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j == w - 1:
                    if i != h - 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
                else:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for i in range(len(ans)):
        for j in range(4):
            print(ans[i][j], end=" ")
        print()
