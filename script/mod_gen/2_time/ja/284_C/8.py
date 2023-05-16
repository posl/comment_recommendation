def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 処理
    # 連結成分の個数を求める
    # グラフの連結成分の個数は、グラフの頂点数から連結成分の個数を引くことで求めることができる
    # 連結成分の個数は、グラフの頂点数から連結成分の最大値を引くことで求めることができる
    # 連結成分の最大値は、グラフの頂点数から1を引くことで求めることができる
    # 連結成分の最大値は、グラフの頂点数-1
    # 連結成分の個数は、グラフの頂点数-1-連結成分の最大値
    # 連結成分の個数は、グラフの頂点数-1-グラフの頂点数-1
    # 連結成分の個数は、0
    # 連結成分の個数は、0個
    # 出力
    print(N-1)

if __name__ == '__main__':
    main()