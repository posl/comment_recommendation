def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(AB)
    # グラフ作成
    # 頂点0は使わない
    # 頂点iは部屋iに対応
    # 辺は部屋間の移動に対応
    # 部屋1からの移動のみを考える
    # 部屋1からの移動を考えると、
    # 1から移動できる部屋、1から移動できる部屋から移動できる部屋、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋
