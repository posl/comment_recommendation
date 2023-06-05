def is_honest(i, n, a, x, y):
    if i == n:
        for j in range(n):
            if a[j] == 1:
                for k in range(a[j]):
                    if y[j][k] == 1:
                        if a[x[j][k]-1] == 1:
                            if y[x[j][k]-1][0] != 1:
                                return False
                        else:
                            if y[x[j][k]-1][0] != 0:
                                return False
        return True
    else:
        a[i] = 1
        if is_honest(i+1, n, a, x, y):
            return True
        a[i] = 0
        if is_honest(i+1, n, a, x, y):
            return True
        return False
n = int(input())
a = [0] * n
x = []
y = []
for i in range(n):
    a[i] = int(input())
    x.append([0] * a[i])
    y.append([0] * a[i])
    for j in range(a[i]):
        x[i][j], y[i][j] = map(int, input().split())
