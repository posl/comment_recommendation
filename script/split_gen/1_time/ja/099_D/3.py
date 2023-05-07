def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    #print(N, C)
    #print(D)
    #print(c)
    for i in range(C):
        for j in range(C):
            D[i][j] = min(D[i][j], D[i][0] + D[0][j])
    #print(D)
    #print(c)
    a = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            a[(i + j) % 3][c[i][j] - 1] += 1
    #print(a)
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                #print(i, j, k)
                x = 0
                for l in range(C):
                    x += D[l][i] * a[0][l]
                    x += D[l][j] * a[1][l]
                    x += D[l][k] * a[2][l]
                ans = min(ans, x)
    print(ans)
