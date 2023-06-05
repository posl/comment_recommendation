def f(x, y):
    if x >= 0 and x < n and y >= 0 and y < n and s[x][y] == -1:
        s[x][y] = s[i][j] + 1
        q.append((x, y))
n, m = map(int, input().split())
s = [[-1]*n for i in range(n)]
s[0][0] = 0
q = [(0, 0)]
while len(q) > 0:
    i, j = q.pop(0)
    f(i+1, j)
    f(i-1, j)
    f(i, j+1)
    f(i, j-1)
for i in range(n):
    for j in range(n):
        if s[i][j] == -1:
            print(-1, end=' ')
        else:
            print(s[i][j], end=' ')
    print()

if __name__ == '__main__':
    f()