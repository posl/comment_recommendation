def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            for k in range(8):
                x = i
                y = j
                s = str(a[x][y])
                for l in range(n - 1):
                    x += dx[k]
                    y += dy[k]
                    s += str(a[x][y])
                ans = max(ans, int(s))
    print(ans)
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
