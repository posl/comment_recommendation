def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x_y_r = [list(map(int, input().split())) for _ in range(N)]
    #円の中心と点の距離を求める
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    #点と円の位置関係
    def position(x1, y1, x2, y2, r):
        d = dist(x1, y1, x2, y2)
        if d > r:
            return 0
        elif d == r:
            return 1
        else:
            return 2
    #点と円の位置関係が2つとも異なる場合は通ることができない
    p_s = [position(s_x, s_y, x, y, r) for x, y, r in x_y_r]
    p_t = [position(t_x, t_y, x, y, r) for x, y, r in x_y_r]
    if all(p_s[i] == p_t[i] for i in range(N)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()