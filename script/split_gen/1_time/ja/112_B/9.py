def main():
    # 標準入力から N, T を取得
    N, T = map(int, input().split())
    # 標準入力から N 個の (c_i, t_i) を取得
    routes = [tuple(map(int, input().split())) for _ in range(N)]
    # コストが最小となる経路のコストを求める
    # 時間 T 以内に帰宅できる経路のうち、コストが最小となる経路のコストを求める
    # ただし、どの経路を使っても時間 T 以内に帰宅できない場合、TLE と出力せよ。
    min_cost = min([c for c, t in routes if t <= T], default="TLE")
    # コストが最小となる経路のコストを出力
    print(min_cost)
