def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]
    cities = sorted(cities, key=lambda x: x[1])
    prefectures = [0] * N
    for i in range(M):
        p, y = cities[i]
        prefectures[p-1] += 1
        cities[i].append(prefectures[p-1])
    cities = sorted(cities, key=lambda x: x[0])
    for i in range(M):
        p, y, n = cities[i]
        print("{:0>6}{:0>6}".format(p, n))

if __name__ == '__main__':
    main()