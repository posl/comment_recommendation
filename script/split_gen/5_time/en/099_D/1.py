def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    c1 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            c1[(i + j) % 3][c[i][j] - 1] += 1
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for x in range(C):
                    tmp += D[x][i] * c1[0][x]
                for x in range(C):
                    tmp += D[x][j] * c1[1][x]
                for x in range(C):
                    tmp += D[x][k] * c1[2][x]
                ans = min(ans, tmp)
    print(ans)
