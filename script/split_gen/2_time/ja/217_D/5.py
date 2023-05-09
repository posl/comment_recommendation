def main():
    L, Q = map(int, input().split())
    #区間を管理するリスト
    interval_list = [(0, L)]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            for i in range(len(interval_list)):
                #区間の左端がxより小さく、区間の右端がxより大きい場合
                if interval_list[i][0] < x and interval_list[i][1] > x:
                    #区間を分割し、interval_listに格納する
                    interval_list.append((interval_list[i][0], x))
                    interval_list.append((x, interval_list[i][1]))
                    #分割した区間を削除する
                    interval_list.pop(i)
                    break
        else:
            for i in range(len(interval_list)):
                #区間の左端がxより小さく、区間の右端がxより大きい場合
                if interval_list[i][0] < x and interval_list[i][1] > x:
                    #区間の長さを出力する
                    print(interval_list[i][1] - interval_list[i][0])
                    break
