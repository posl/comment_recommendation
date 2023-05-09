def main():
    # 標準入力から N と T を取得する
    n, t = map(int, input().split())
    # N 個の帰宅経路を取得する
    c = []
    t = []
    for i in range(n):
        c_tmp, t_tmp = map(int, input().split())
        c.append(c_tmp)
        t.append(t_tmp)
    # コストが最小となる経路のコストを求める
    # ただし、どの経路を使っても時間 T 以内に帰宅できない場合、TLE と出力する
    cost = 1001
    for i in range(n):
        if t[i] <= t:
            if cost > c[i]:
                cost = c[i]
    if cost == 1001:
        print('TLE')
    else:
        print(cost)
