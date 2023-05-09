def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    
    # 3色に分ける
    C1 = [] # 0, 3, 6, 9, ...
    C2 = [] # 1, 4, 7, 10, ...
    C3 = [] # 2, 5, 8, 11, ...
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1.append(c[i][j] - 1)
            elif (i + j) % 3 == 1:
                C2.append(c[i][j] - 1)
            else:
                C3.append(c[i][j] - 1)
    
    # 3色に分けたものをそれぞれ色を変えるコストの最小値を求める
    cost = [[0] * C for _ in range(3)]
    for i in range(C):
        for j in range(C):
            cost[0][i] += D[j][i] * C1.count(j)
            cost[1][i] += D[j][i] * C2.count(j)
            cost[2][i] += D[j][i] * C3.count(j)
    
    # 3色に分けたものをそれぞれ色を変えるコストの最小値の最小値を求める
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

if __name__ == '__main__':
    main()