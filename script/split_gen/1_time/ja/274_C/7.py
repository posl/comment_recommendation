def main():
    n = int(input())
    a = list(map(int, input().split()))
    # アメーバの親を記録する配列
    parents = [0] * (2 * n + 2)
    # 親を記録
    for i in range(n):
        parents[2 * i + 1] = a[i]
        parents[2 * i + 2] = a[i]
    # 各アメーバの親を辿ってアメーバ1になるまでの距離を計算
    for i in range(2, 2 * n + 2):
        parents[i] = parents[parents[i]] + 1
    # 計算結果を出力
    for i in range(1, 2 * n + 2):
        print(parents[i])
