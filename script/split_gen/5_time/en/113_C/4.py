def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: (x[0], x[1]))
    prefectures = [0] * (n + 1)
    for p, y in p_y:
        prefectures[p] += 1
    city_numbers = [0] * (n + 1)
    for i in range(1, n + 1):
        city_numbers[i] = city_numbers[i - 1] + prefectures[i]
    for p, y in p_y:
        print('{0:06}{1:06}'.format(p, city_numbers[p]))
        city_numbers[p] += 1
