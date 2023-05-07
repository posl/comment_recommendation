def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        p, y = map(int, input().split())
        city.append([i, p, y])
    city.sort(key=lambda x: x[1])
    city.sort(key=lambda x: x[2])
    pref = [0 for i in range(N+1)]
    for i in range(M):
        pref[city[i][1]] += 1
        city[i].append(pref[city[i][1]])
    city.sort(key=lambda x: x[0])
    for i in range(M):
        print("{0:06d}{1:06d}".format(city[i][1], city[i][3]))

if __name__ == '__main__':
    main()