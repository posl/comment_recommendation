def main():
    n = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    # 1. (s_x, s_y)と(t_x, t_y)が同じ円の上にあるかを判定する
    # 2. (s_x, s_y)と(t_x, t_y)が同じ円の上にない場合、
    #    (s_x, s_y)と(t_x, t_y)の間に、他の円が存在しないかを判定する
    # 1. (s_x, s_y)と(t_x, t_y)が同じ円の上にあるかを判定する
    for x, y, r in circles:
        if ((x - s_x)**2 + (y - s_y)**2 - r**2)**2 <= 1e-10:
            if ((x - t_x)**2 + (y - t_y)**2 - r**2)**2 <= 1e-10:
                print('Yes')
                return
    # 2. (s_x, s_y)と(t_x, t_y)が同じ円の上にない場合、
    #    (s_x, s_y)と(t_x, t_y)の間に、他の円が存在しないかを判定する
    for x1, y1, r1 in circles:
        for x2, y2, r2 in circles:
            if (x1, y1, r1) == (x2, y2, r2):
                continue
            # 2-1. (s_x, s_y)と(t_x, t_y)の間に、他の円が存在するかを判定する
            if ((x1 - s_x)**2 + (y1 - s_y)**2 - r1**2)**2 <= 1e-10:
                if ((x2 - t_x)**2 + (y2 - t_y)**2 - r2**2)**2 <= 1e

if __name__ == '__main__':
    main()