def main():
    #入力
    N = int(input())
    s_x, s_y, t_x, t_y = map(int,input().split())
    x = [0] * N
    y = [0] * N
    r = [0] * N
    for i in range(N):
        x[i], y[i], r[i] = map(int,input().split())
    #円周上にある点のみを通って行けるかどうかの判定
    def judge(x1, y1, r1, x2, y2, r2):
        #2つの円の中心距離
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
        #2つの円の中心距離が2つの円の半径の和より大きい場合は行けない
        if d > r1 + r2:
            return False
        #2つの円が重なっている場合は行けない
        if d < abs(r1 - r2):
            return False
        return True
    #円周上にある点のみを通って行けるかどうかの判定
    for i in range(N):
        if judge(s_x, s_y, 0, x[i], y[i], r[i]) and judge(t_x, t_y, 0, x[i], y[i], r[i]):
            print("Yes")
            return
    print("No")
