def get_input():
    n = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    return n, s_x, s_y, t_x, t_y, circles

if __name__ == '__main__':
    get_input()