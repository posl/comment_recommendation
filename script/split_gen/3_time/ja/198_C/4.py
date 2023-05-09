def main():
    r, x, y = map(int, input().split())
    # 距離を求める
    d = ((x**2)+(y**2))**(1/2)
    # 距離をrで割った余りが0なら、距離をrで割った商が答え
    if d%r == 0:
        print(int(d/r))
    # 距離をrで割った余りが0でないなら、距離をrで割った商に1を足したものが答え
    else:
        print(int(d/r)+1)
