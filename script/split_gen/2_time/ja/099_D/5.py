def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    count = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            count[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * count[0][l]
                    tmp += D[l][j] * count[1][l]
                    tmp += D[l][k] * count[2][l]
                ans = min(ans, tmp)
    print(ans)
