def main():
    N, M = map(int, input().split())
    # N:島の数, M:橋の数
    bridge = [list(map(int, input().split())) for _ in range(M)]
    # bridge:橋の情報
    # bridge[i][0]:橋iの島A
    # bridge[i][1]:橋iの島B
    # bridge[i][2]:橋iの崩落フラグ(0:崩落前, 1:崩落後)
    # bridge[i][3]:橋iの崩落後の不便さ
    # 島の数がNの場合、最大不便さはN-1
    # これを初期値として設定する
    inconvenience = N - 1
    # 橋の情報を逆順に取得する
    for i in range(M - 1, -1, -1):
        # 橋iが崩落していない場合
        if bridge[i][2] == 0:
            # 橋iが崩落したことを記録する
            bridge[i][2] = 1
            # 橋iの崩落後の不便さを記録する
            bridge[i][3] = inconvenience
            # 橋iの島Aから島Bを経由して島Aに行く場合の不便さを計算する
            # 橋iの島Aから島Bを経由して島Aに行く場合の不便さは
            # 橋iの島Aから島Bを経由して島Aに行く場合の不便さ + 1
            inconvenience += 1
        # 橋iが崩落している場合
        else:
            # 橋iの崩落後の不便さを記録

if __name__ == '__main__':
    main()