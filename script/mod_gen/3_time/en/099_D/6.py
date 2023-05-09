def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 3色のコストを求める
    cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cost[(i + j) % 3][c[i][j] - 1] += 1
    # 3色のコストを組み合わせたコストを求める
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += cost[0][l] * D[l][i]
                    tmp += cost[1][l] * D[l][j]
                    tmp += cost[2][l] * D[l][k]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    solve()