def main():
    n = int(input())
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    # 2点間の距離を計算
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
    # 2点間の距離が等しいものの個数を数える
    d = {}
    for i in range(n):
        for j in range(i + 1, n):
            if dist[i][j] in d:
                d[dist[i][j]] += 1
            else:
                d[dist[i][j]] = 1
    # 2点間の距離が等しいものが2個以上あれば、
    # 2点間の距離が等しいものの個数が答え
    for v in d.values():
        if v >= 2:
            print(v + 1)
            return
    # 2点間の距離が等しいものが1個もなければ、
    # 2点間の距離が等しいものがないので、
    # 2点間の距離が等しいものの個数は1
    print(1)

if __name__ == '__main__':
    main()