def main():
    N, M = map(int, input().split())
    L, R = [], []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ
    print(min(R) - max(L) + 1 if min(R) - max(L) + 1 > 0 else 0)
