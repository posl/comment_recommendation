def dfs(i, x, y):
    if i == n:
        for j in range(n):
            if x[j] == 1:
                for k in range(a[j]):
                    if x[b[j][k]-1] != y[j][k]:
                        return 0
        return sum(x)
    else:
        x[i] = 1
        if dfs(i+1, x, y) == 0:
            x[i] = 0
            return dfs(i+1, x, y)
        else:
            return dfs(i+1, x, y)
n = int(input())
a = [0]*n
b = [[] for i in range(n)]
y = [[] for i in range(n)]
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        x, y[i][j] = map(int, input().split())
        b[i].append(x)
x = [0]*n
print(dfs(0, x, y))

if __name__ == '__main__':
    dfs()