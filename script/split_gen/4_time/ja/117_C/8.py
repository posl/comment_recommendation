def main():
    # データ入力
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    # 座標の重複を削除してソートし、隣り合う座標の差を計算
    x = sorted(list(set(x)))
    d = [x[i+1] - x[i] for i in range(len(x)-1)]
    # 差の大きい順に並び替えて、前から n-1 個の差を足し合わせる
    d.sort(reverse=True)
    print(sum(d[n-1:]))
