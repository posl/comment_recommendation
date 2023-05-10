def main():
    n, m = map(int, input().split())
    cities = []
    for i in range(m):
        p, y = map(int, input().split())
        cities.append([p, y, i])
    cities.sort(key=lambda x: (x[0], x[1]))
    prefecture = cities[0][0]
    count = 0
    for i in range(m):
        if prefecture == cities[i][0]:
            count += 1
        else:
            prefecture = cities[i][0]
            count = 1
        cities[i].append(count)
    cities.sort(key=lambda x: x[2])
    for i in range(m):
        print('{:06d}{:06d}'.format(cities[i][0], cities[i][3]))

if __name__ == '__main__':
    main()