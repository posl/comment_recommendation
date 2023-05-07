def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 1,2,3の色をそれぞれ0,1,2としておく
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    # 3種類の色のそれぞれのマスの数を数える
    c0 = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            c0[(i+j)%3][c[i][j]] += 1
    # 各色のコストを求める
    cost = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[j][k] * c0[i][k]
    # 全探索
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)
