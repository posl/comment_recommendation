def main():
    # 標準入力の取得
    p, q, r = map(int, input().split())
    # 飛行時間の和の最小値を出力
    print(min(p + q, q + r, r + p))
