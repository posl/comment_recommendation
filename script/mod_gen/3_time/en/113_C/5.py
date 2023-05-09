def main():
    N, M = map(int, input().split())
    cities = []
    for _ in range(M):
        P, Y = map(int, input().split())
        cities.append([P, Y])
    cities.sort(key=lambda x : x[1])
    p = 0
    y = 0
    for i in range(M):
        if cities[i][0] != p:
            p = cities[i][0]
            y = 1
        else:
            y += 1
        print("{0:06d}".format(p) + "{0:06d}".format(y))

if __name__ == '__main__':
    main()