def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    # print(circles)
    # 2点間の距離を求める
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 2点間の距離が円の半径より大きければOK
    for x, y, r in circles:
        if dist(s_x, s_y, x, y) <= r and dist(t_x, t_y, x, y) <= r:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()