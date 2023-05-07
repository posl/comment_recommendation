def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(C)]
    c = [list(map(int, input().split())) for i in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                D[j][k] = min(D[j][k], D[j][i] + D[i][k])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += D[(i + j) % 3][c[i][j] - 1]
    print(ans)
