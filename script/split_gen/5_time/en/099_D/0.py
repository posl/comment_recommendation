def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # mod3ごとに色を分類
    color = [[], [], []]
    for i in range(N):
        for j in range(N):
            color[(i+j) % 3].append(c[i][j]-1)
    # 色の組み合わせごとにそれぞれの色に塗り替えるときのコストを求める
    cost = [[0]*C for _ in range(C)]
    for i in range(C):
        for j in range(C):
            for k in color[0]:
                cost[i][j] += D[k][i]
            for k in color[1]:
                cost[i][j] += D[k][j]
            for k in color[2]:
                cost[i][j] += D[k][j]
    # 3色をそれぞれで塗り替えたときの最小コストを求める
    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, cost[i][j]+cost[j][k]+cost[k][i])
    print(ans)
