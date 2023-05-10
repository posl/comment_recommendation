def main():
    n = int(input())
    a = [[0 for i in range(2001)] for j in range(2001)]
    for i in range(n):
        x, y = map(int, input().split())
        a[x+1000][y+1000] = 1
    dx = [1, 1, 0, -1, -1, 0]
    dy = [-1, 0, 1, 1, 0, -1]
    ans = 0
    for i in range(2001):
        for j in range(2001):
            if a[i][j] == 1:
                ans += 1
                q = []
                q.append([i, j])
                a[i][j] = 0
                while len(q) > 0:
                    x, y = q.pop()
                    for k in range(6):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 2001 and 0 <= ny < 2001 and a[nx][ny] == 1:
                            q.append([nx, ny])
                            a[nx][ny] = 0
    print(ans)

if __name__ == '__main__':
    main()