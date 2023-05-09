def main():
    n = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    if is_reachable(circles, s_x, s_y, t_x, t_y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()