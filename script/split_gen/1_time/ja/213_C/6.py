def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # 重複を排除した座標を得る
    A = sorted(set([ab[0] for ab in AB]))
    B = sorted(set([ab[1] for ab in AB]))
    # 座標の変換
    for i in range(N):
        # 重複を排除した座標の順番を得る
        a = bisect.bisect_left(A, AB[i][0])
        b = bisect.bisect_left(B, AB[i][1])
        print(a+1, b+1)
