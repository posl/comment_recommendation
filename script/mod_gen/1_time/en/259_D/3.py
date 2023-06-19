def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    C = []
    for i in range(N):
        x, y, r = map(int, input().split())
        C.append((x, y, r))
    
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    def check(x, y):
        for cx, cy, r in C:
            d1 = dist(x, y, cx, cy)
            d2 = dist(s_x, s_y, cx, cy)
            d3 = dist(t_x, t_y, cx, cy)
            if d1 < r and d2 > r and d3 > r:
                return False
        return True
    
    if check(s_x, s_y) and check(t_x, t_y):
        print("Yes")
    else:
        print("No")
main()
