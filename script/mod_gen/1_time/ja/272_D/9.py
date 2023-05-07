def solve():
    N, M = map(int, input().split())
    #マス目の最大距離
    MAX = 2 * N * N
    #マス目の最大距離までの最小操作回数
    dist = [MAX] * (MAX + 1)
    dist[0] = 0
    #マス目の最大距離までの最小操作回数を更新
    for i in range(1, MAX + 1):
        dist[i] = min(dist[i], dist[i - 1] + 1)
        for j in range(1, i):
            if (i - j) * (i - j) > M:
                break
            if (M - (i - j) * (i - j)) % i == 0:
                dist[i] = min(dist[i], dist[j] + (M - (i - j) * (i - j)) // i)
    #マス目の最大距離までの最小操作回数を出力
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (i - 1) * (i - 1) + (j - 1) * (j - 1) > MAX:
                print(-1, end=' ')
            else:
                print(dist[(i - 1) * (i - 1) + (j - 1) * (j - 1)], end=' ')
        print()

if __name__ == '__main__':
    solve()