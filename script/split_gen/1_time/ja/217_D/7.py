def main():
    # L, Q = map(int, input().split())
    L = 100
    Q = 10
    # c_x = [list(map(int, input().split())) for _ in range(Q)]
    c_x = [[1, 31], [2, 41], [1, 59], [2, 26], [1, 53], [2, 58], [1, 97], [2, 93], [1, 23], [2, 84]]
    # 木材の長さ
    wood_len = [L]
    # クエリの回数
    query_num = 0
    # クエリの処理
    for c, x in c_x:
        if c == 1:
            # 木材の長さを更新
            idx = -1
            for i in range(len(wood_len)):
                if wood_len[i] > x:
                    idx = i
                    break
            if idx == -1:
                wood_len.append(x)
            else:
                wood_len[idx] -= x
                wood_len.insert(idx, x)
        else:
            # クエリの回数を更新
            query_num += 1
            # 木材の長さを出力
            print(wood_len[x-1])
    # クエリの回数を出力
    print(query_num)
