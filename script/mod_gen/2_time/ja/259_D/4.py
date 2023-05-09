def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xy = []
    for i in range(N):
        x, y, r = map(int, input().split())
        xy.append((x, y, r))
    #print(xy)
    for i in range(N):
        if ((s_x - xy[i][0])**2 + (s_y - xy[i][1])**2) ** 0.5 < xy[i][2]:
            if ((t_x - xy[i][0])**2 + (t_y - xy[i][1])**2) ** 0.5 < xy[i][2]:
                print("No")
                return 0
    print("Yes")
    return 0

if __name__ == '__main__':
    main()