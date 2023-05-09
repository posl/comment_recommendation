def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 1. 点数の計算
    # 2. 降順ソート
    # 3. K番目の人の点数を取得
    # 4. 各人の点数がK番目の点数以上か判定
    # 1. 点数の計算
    # 2. 降順ソート
    # 3. K番目の人の点数を取得
    # 4. 各人の点数がK番目の点数以上か判定
    P = sorted([sum(p) for p in P], reverse=True)
    Kth = P[K-1]
    # 4. 各人の点数がK番目の点数以上か判定
    for p in [sum(p) for p in P]:
        if p >= Kth:
            print("Yes")
        else:
            print("No")
