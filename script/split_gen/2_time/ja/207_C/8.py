def main():
    N = int(input())
    # 1,2,3,4のリストを作成
    t = [0] * N
    l = [0] * N
    r = [0] * N
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())
    # 重複を排除した区間のリストを作成
    interval = []
    for i in range(N):
        if t[i] == 1:
            interval.append((l[i], r[i]))
        elif t[i] == 2:
            interval.append((l[i], r[i] - 1))
        elif t[i] == 3:
            interval.append((l[i] + 1, r[i]))
        else:
            interval.append((l[i] + 1, r[i] - 1))
    # 重複を排除した区間のリストをソート
    interval.sort()
    # 重複を排除した区間のリストの要素を順番に取り出す
    ans = 0
    for i in range(N):
        # 取り出した要素をtmpとする
        tmp = interval[i]
        # tmpの右端より小さい区間のリストを作成
        tmp_list = []
        for j in range(N):
            if interval[j][1] < tmp[1]:
                tmp_list.append(interval[j])
        # tmp_listの要素を順番に取り出す
        for j in range(len(tmp_list)):
            # 取り出した要素をtmp2とする
            tmp2 = tmp_list[j]
            # tmpの左端がtmp2の左端より小さいかつtmpの左端がtmp2の右端より小さいか
            if tmp[0] > tmp2[0] and tmp[0] < tmp2[1]:
                ans += 1
    print(ans)
