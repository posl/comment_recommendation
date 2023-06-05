def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: (x[0], x[1]))
    city_id = [0] * m
    city_cnt = [0] * (n + 1)
    for i in range(m):
        city_cnt[p_y[i][0]] += 1
        city_id[i] = [p_y[i][0], city_cnt[p_y[i][0]]]
    city_id.sort(key=lambda x: x[1])
    for i in range(m):
        print(str(city_id[i][0]).zfill(6) + str(city_id[i][1]).zfill(6))
