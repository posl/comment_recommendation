def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        cities.append(list(map(int, input().split())) + [i])
    cities.sort(key=lambda x: x[1])
    prefecture = 0
    counter = 1
    for i in range(M):
        if prefecture != cities[i][0]:
            counter = 1
            prefecture = cities[i][0]
        cities[i][0] = str(cities[i][0])
        cities[i][1] = str(counter).zfill(6)
        cities[i][2] = str(cities[i][2]).zfill(6)
        counter += 1
    cities.sort(key=lambda x: x[3])
    for i in range(M):
        print(cities[i][0] + cities[i][1] + cities[i][2])

if __name__ == '__main__':
    main()