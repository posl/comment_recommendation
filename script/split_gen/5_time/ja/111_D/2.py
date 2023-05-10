def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline())
    XY = [list(map(int, readline().split())) for _ in range(N)]
    # 処理
    # すべての点について、x座標とy座標が同じであるか
    x_same = True
    y_same = True
    for x, y in XY:
        if x != XY[0][0]:
            x_same = False
        if y != XY[0][1]:
            y_same = False
    if x_same == False and y_same == False:
        print(-1)
        return
    # x座標が同じ
    if x_same:
        # x座標が同じなら、y座標の差が奇数である
        y_diff = [abs(y - XY[0][1]) for x, y in XY]
        y_diff_odd = [y for y in y_diff if y % 2 == 1]
        if len(y_diff_odd) > 0 and len(y_diff_odd) < len(y_diff):
            print(-1)
            return
        # 差が奇数である場合、y座標が同じになるようにする
        if len(y_diff_odd) > 0:
            for i in range(N):
                if y_diff[i] % 2 == 0:
                    XY[i][1] += 1
                    y_diff[i] += 1
                    break
        # y座標の差を2で割ったものが、ロボットアームの本数
        m = max(y_diff) // 2
        d = [2 * m - y for y in y_diff]
        w = []
        for x, y in XY:
            w_j = ''
            for i in range(m):
                if y > 0:
                    w_j += 'D'
                    y -= 1
                else:
                    w_j += 'U'
                    y += 1
            w.append(w_j)
    # y座標が同じ
    if y
