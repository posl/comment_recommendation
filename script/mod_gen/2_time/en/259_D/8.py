def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    s = (s_x, s_y)
    t = (t_x, t_y)
    for x, y, r in circles:
        if (s[0] - x) ** 2 + (s[1] - y) ** 2 < r ** 2 and (t[0] - x) ** 2 + (t[1] - y) ** 2 < r ** 2:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()