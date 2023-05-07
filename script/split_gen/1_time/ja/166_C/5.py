def main():
    #入力
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #初期化
    good = [1] * N
    #処理
    for a, b in AB:
        if H[a - 1] > H[b - 1]:
            good[b - 1] = 0
        elif H[a - 1] < H[b - 1]:
            good[a - 1] = 0
        else:
            good[a - 1] = 0
            good[b - 1] = 0
    #出力
    print(sum(good))
