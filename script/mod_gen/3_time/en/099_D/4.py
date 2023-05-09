def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 3色ごとのマスの個数
    count = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            count[(i + j) % 3][c[i][j] - 1] += 1
    # 3色の最小コスト
    cost = [[0] * C for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[j][k] * count[i][k]
    # 3色の最小コストの最小値
    print(min(sum(cost, [])))

if __name__ == '__main__':
    main()