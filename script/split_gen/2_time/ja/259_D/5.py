def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    center = []
    radius = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        center.append((x, y))
        radius.append(r)
    print("Yes" if solve(s_x, s_y, t_x, t_y, center, radius) else "No")
