def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                cost = 0
                for l in range(C):
                    cost += D[l][i] * cnt[0][l]
                    cost += D[l][j] * cnt[1][l]
                    cost += D[l][k] * cnt[2][l]
                ans = min(ans, cost)
    print(ans)
