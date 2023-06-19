def findmin(x, y, z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z
N, C = map(int, input().split())
D = [[0 for i in range(C)] for j in range(C)]
for i in range(C):
    D[i] = list(map(int, input().split()))
C = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    C[i] = list(map(int, input().split()))
d = [[0 for i in range(C)] for j in range(C)]
for i in range(C):
    for j in range(C):
        d[i][j] = D[i][j]
for k in range(C):
    for i in range(C):
        for j in range(C):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
ans = 1 << 30
for i in range(C):
    for j in range(C):
        if i != j:
            tmp = 0
            for k in range(N):
                for l in range(N):
                    if (k + l) % 3 == 0:
                        tmp += d[C[k][l] - 1][i]
                    elif (k + l) % 3 == 1:
                        tmp += d[C[k][l] - 1][j]
                    else:
                        tmp += d[C[k][l] - 1][0]
            ans = min(ans, tmp)
print(ans)

if __name__ == '__main__':
    findmin()