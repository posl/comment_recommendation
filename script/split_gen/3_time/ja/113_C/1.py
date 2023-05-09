def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    p = np.array(p)
    y = np.array(y)
    # 都道府県ごとに市の誕生年をソート
    p_sorted = np.argsort(p)
    y_sorted = np.argsort(y[p_sorted])
    # 誕生年の順番を都道府県の順番に変換
    y_sorted = p_sorted[y_sorted]
    # 都道府県ごとに市の誕生年の順番を取得
    y_sorted = np.argsort(y_sorted)
    # 認識番号を出力
    for i in range(m):
        print('{:06d}{:06d}'.format(p[i], y_sorted[i] + 1))
