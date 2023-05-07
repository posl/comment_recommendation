def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 1, 2, 3の色について、それぞれの色が選ばれた時のコストを計算
    cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cost[(i + j) % 3][c[i][j] - 1] += 1
    # コストが最小になるように色を割り当てる
    ans = 10 ** 18
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                tmp += cost[0][i] * D[i][j]
                tmp += cost[1][j] * D[j][k]
                tmp += cost[2][k] * D[k][i]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()