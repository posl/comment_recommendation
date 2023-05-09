def main():
    N, A, B = map(int, input().split())
    S = input()
    if N == 1:
        print(0)
        return
    # 連続する同じ文字の個数をカウント
    # 例: S = "rrefa" なら cnt = [2, 1, 1]
    cnt = []
    now = S[0]
    cnt_now = 1
    for i in range(1, N):
        if S[i] == now:
            cnt_now += 1
        else:
            cnt.append(cnt_now)
            now = S[i]
            cnt_now = 1
    cnt.append(cnt_now)
    # print(cnt)
    # 連続する同じ文字の個数を使って、
    # 1. 全て同じ文字の場合
    # 2. 2 文字のみ違う場合
    # 3. 3 文字のみ違う場合
    # 4. 4 文字のみ違う場合
    # 5. それ以外
    # の場合を考える
    # 1. 全て同じ文字の場合
    # 1 文字のみ違う場合と同じ
    # 2. 2 文字のみ違う場合
    # 2 文字のみ違う場合と同じ
    # 3. 3 文字のみ違う場合
    # 2 文字のみ違う場合と同じ
    # 4. 4 文字のみ違う場合
    # 2 文字のみ違う場合と同じ
    # 5. それ以外
    # 2 文字のみ違う場合と同じ
    # 1. 全て同じ文字の場合
    if len(cnt) == 1:
        print(0)
        return
    # 2. 2 文字のみ違う場合
    if len(cnt) == 2:
        print(min(A, B))
        return
    # 3. 3 文字

if __name__ == '__main__':
    main()