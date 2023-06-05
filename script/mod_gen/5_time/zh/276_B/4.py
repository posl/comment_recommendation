def print_city(road):
    road.sort(key=lambda x: (x[0], x[1]))
    city = [0] * (N + 1)
    for i in range(M):
        city[road[i][0]] += 1
        city[road[i][1]] += 1
    for i in range(1, N + 1):
        print(city[i], end=' ')
        for j in range(M):
            if i == road[j][0]:
                print(road[j][1], end=' ')
            elif i == road[j][1]:
                print(road[j][0], end=' ')
        print()

if __name__ == '__main__':
    print_city()