def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    # 重さの和の最大値
    max_sum = 0
    # 重さの和の最小値
    min_sum = 0
    # 重さの和の最大値と最小値を計算する
    for i in range(n):
        max_sum += a[i]
        min_sum += a[i]
    # 重さの和の最大値と最小値がwより大きい場合は0を返す
    if max_sum < w or min_sum > w:
        print(0)
        return
    # 重さの和の最大値と最小値の間の数値の個数を返す
    print(max_sum - min_sum + 1)
