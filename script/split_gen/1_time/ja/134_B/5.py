def main():
    # 入力
    N, D = map(int, input().split())
    # 処理
    # 条件を満たすために配置する必要のある監視員の人数の最小値
    min_num = N // (2 * D + 1)
    if N % (2 * D + 1) != 0:
        min_num += 1
    # 出力
    print(min_num)
