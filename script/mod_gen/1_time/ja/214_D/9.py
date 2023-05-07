def calc_f(n, edges):
    # 頂点iから頂点jまでの最短パスに含まれる辺の重みの最大値
    f = [[0] * n for _ in range(n)]
    for s, t, w in edges:
        f[s - 1][t - 1] = w
        f[t - 1][s - 1] = w
    # ワーシャルフロイド法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f[i][j] = max(f[i][j], f[i][k] + f[k][j])
    return f

if __name__ == '__main__':
    calc_f()