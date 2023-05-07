def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 3色のリストを作る
    color = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1
    # 3色のリストを3色のコストにする
    cost = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[k][j] * color[i][k]
    # 3色のコストを全探索する
    ans = 10**9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)
