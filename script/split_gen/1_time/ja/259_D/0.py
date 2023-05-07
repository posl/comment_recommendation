def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x_y_r = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        x_y_r.append((x, y, r))
    
    #円の中心と点sとtの距離
    s_dist = [((s_x - x)**2 + (s_y - y)**2)**(1/2) for x, y, r in x_y_r]
    t_dist = [((t_x - x)**2 + (t_y - y)**2)**(1/2) for x, y, r in x_y_r]
    #円の中心と点sとtの距離が半径より小さければ通れる
    for i in range(N):
        if s_dist[i] <= x_y_r[i][2] and t_dist[i] <= x_y_r[i][2]:
            print("Yes")
            return
    #円の中心と点sとtの距離の差が半径より小さければ通れる
    for i in range(N):
        for j in range(N):
            if abs(s_dist[i] - t_dist[j]) <= x_y_r[i][2]:
                print("Yes")
                return
    print("No")
