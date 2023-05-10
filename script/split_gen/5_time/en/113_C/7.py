def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: x[1])
    p_y2 = [[p_y[i][0], p_y[i][1], i+1] for i in range(m)]
    p_y2.sort(key=lambda x: x[0])
    p_y2 = [[p_y2[i][0], p_y2[i][1], p_y2[i][2], str(p_y2[i][0]).zfill(6), str(p_y2[i][2]).zfill(6)] for i in range(m)]
    for i in range(m):
        print(p_y2[i][3]+p_y2[i][4])
