def make_list(n):
    #nが1の時のリスト
    list1 = [1]
    #nが6の時のリスト
    list6 = [6]
    #nが9の時のリスト
    list9 = [9]
    #nが6の時のリストの要素数
    count6 = 1
    #nが9の時のリストの要素数
    count9 = 1
    #nが1の時のリストの要素数
    count1 = 1
    #nが6の時のリストの要素数がnより大きくなるまでループ
    while count6 < n:
        #nが6の時のリストの要素数がnより大きくなるまでループ
        for i in range(count6):
            #nが6の時のリストにnが6の時のリストの要素数を6で掛けた数を追加
            list6.append(list6[i]*6)
            #nが6の時のリストの要素数を1増やす
            count6 += 1
            #nが6の時のリストの要素数がnより大きくなったらループを抜ける
            if count6 >= n:
                break
    #nが9の時のリストの要素数がnより大きくなるまでループ
    while count9 < n:
        #nが9の時のリストの要素数がnより大きくなるまでループ
        for i in range(count9):
            #nが9の時のリストにnが9の時のリストの要素数を9で掛けた数を追加
            list9.append(list9[i]*9)
            #nが9の時のリストの要素数を1増やす
            count9 += 1
            #nが9の時のリストの要素数がnより大きくなったらループを抜ける
            if count9

if __name__ == '__main__':
    make_list()