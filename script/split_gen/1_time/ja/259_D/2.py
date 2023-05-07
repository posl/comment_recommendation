def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x_y_r = [list(map(int, input().split())) for _ in range(N)]
    print('Yes' if solve(s_x, s_y, t_x, t_y, x_y_r) else 'No')
