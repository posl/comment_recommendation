def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: x[1])
    p_count = [0] * n
    city_id = [0] * m
    for i in range(m):
        p_count[p_y[i][0] - 1] += 1
        city_id[i] = '{:06d}{:06d}'.format(p_y[i][0], p_count[p_y[i][0] - 1])
    for i in range(m):
        print(city_id[i])
