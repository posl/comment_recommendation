def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # Xの値を0から始めるために1を引く
    X -= 1
    # 0からNまでのリストを作成
    # 0:未知, 1:知っている, 2:知られている
    ans = [0] * N
    # Xの友達は知っている
    ans[X] = 1
    # Xの友達を知っている人数
    cnt = 1
    # Xの友達の友達を知っている人数
    cnt2 = 0
    # Xの友達の友達を知っている人数が0になるまで繰り返す
    while cnt2 != 0:
        # Xの友達の友達を知っている人数を0にする
        cnt2 = 0
        # Xの友達の友達を知っている人数を数える
        for i in range(N):
            if ans[i] == 2:
                cnt2 += 1
        # Xの友達の友達を知っている人数が0になったら終了
        if cnt2 == 0:
            break
        # Xの友達の友達を知っている人数を0にする
        cnt2 = 0
        # Xの友達の友達を知っている人数を数える
        for i in range(N):
            if ans[i] == 2:
                cnt2 += 1
        # Xの友達の友達を知っている人数が0になったら終了
        if cnt2 == 0:
            break
        # Xの友達の友達を知っている人数を0にする
        cnt2 = 0
        # Xの友達の友達を知っている人数を数える
        for i in range

if __name__ == '__main__':
    main()