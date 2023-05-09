def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] -= 1
    # 余りごとに色ごとの個数を数える
    mod = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3][C[i][j]] += 1
    # 余りごとに色を変えるコストを求める
    cost = [[0] * C for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[j][k] * mod[i][k]
    # 余りごとに最小のコストを求める
    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

if __name__ == '__main__':
    main()