def main():
    # 標準入力受付
    n,m,t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]
    # 持ち時間を計算
    t += a[-1]
    # ボーナス部屋の処理
    for x,y in xy:
        t += y - a[x-1]
    # 結果出力
    print("Yes" if t >= a[-1] else "No")
