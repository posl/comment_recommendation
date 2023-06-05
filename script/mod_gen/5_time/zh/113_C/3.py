def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        city.append(list(map(int, input().split())))
    city.sort(key=lambda x: x[1])
    city_id = [[0 for i in range(2)] for j in range(M)]
    city_id[0][0] = city[0][0]
    city_id[0][1] = 1
    for i in range(1, M):
        if city[i][0] == city_id[i - 1][0]:
            city_id[i][0] = city[i][0]
            city_id[i][1] = city_id[i - 1][1] + 1
        else:
            city_id[i][0] = city[i][0]
            city_id[i][1] = 1
    for i in range(M):
        print(str(city_id[i][0]).zfill(6) + str(city_id[i][1]).zfill(6))

if __name__ == '__main__':
    main()