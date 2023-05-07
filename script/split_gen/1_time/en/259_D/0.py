def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = []
    for i in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    print("Yes") if solve(N, s_x, s_y, t_x, t_y, circles) else print("No")
