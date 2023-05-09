def main():
    n = int(input())
    s = [list(input()) for i in range(n)]
    t = [list(input()) for i in range(n)]
    # 連結成分の左上の座標を求める
    s_x, s_y = find_top_left(s)
    t_x, t_y = find_top_left(t)
    # 連結成分を左上に移動
    s = move(s, s_x, s_y)
    t = move(t, t_x, t_y)
    # 連結成分のサイズを求める
    s_size = find_size(s)
    t_size = find_size(t)
    # 連結成分のサイズが違うときは No
    if s_size != t_size:
        print('No')
        return
    # 連結成分のサイズが同じときは 4 回の回転を試す
    for i in range(4):
        # 連結成分が一致するかを確認する
        if s == t:
            print('Yes')
            return
        # 連結成分を90度回転
        s = rotate(s)
    # 4回回転しても一致しないときは No
    print('No')
