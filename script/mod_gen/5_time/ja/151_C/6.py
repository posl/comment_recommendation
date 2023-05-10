def solve():
    N, M = map(int, input().split())
    # 問題数分のACフラグを作成
    # 問題番号とACフラグのインデックスは-1する
    # False: ACを出していない
    # True: ACを出している
    ac_flag_list = [False] * N
    # 問題数分のWAフラグを作成
    # 問題番号とWAフラグのインデックスは-1する
    # 0: ACを出していない
    # 1以上: ACを出すまでのWA数
    wa_flag_list = [0] * N
    # WA数
    wa_count = 0
    # AC数
    ac_count = 0
    # M回の入力
    for i in range(M):
        p, s = input().split()
        # 問題番号(インデックス)は-1する
        p = int(p) - 1
        # ACの場合
        if s == 'AC':
            # まだACを出していない場合
            if ac_flag_list[p] == False:
                # ACフラグを立てる
                ac_flag_list[p] = True
                # AC数をカウントする
                ac_count += 1
                # その問題のWA数をカウントする
                wa_count += wa_flag_list[p]
        # WAの場合
        else:
            # まだACを出していない場合
            if ac_flag_list[p] == False:
                # その問題のWA数をカウントする
                wa_flag_list[p] += 1
    # 結果を出力する
    print(ac_count, wa_count)

if __name__ == '__main__':
    solve()