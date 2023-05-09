def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 0, 1, 2の色について
    # 0: 1, 2, 3
    # 1: 2, 3, 1
    # 2: 3, 1, 2
    # という順番で塗るときの最小コスト
    min_cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(3):
                min_cost[k][c[i][j] - 1] += D[k][c[i][j] - 1]
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                cost = min_cost[0][i] + min_cost[1][j] + min_cost[2][k]
                ans = min(ans, cost)
    print(ans)
