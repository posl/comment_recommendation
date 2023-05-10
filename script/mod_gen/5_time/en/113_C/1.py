def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        P, Y = map(int, input().split())
        cities.append([P, Y, i])
    cities.sort(key=lambda x: (x[0], x[1]))
    pref = cities[0][0]
    cnt = 1
    for i in range(M):
        if pref == cities[i][0]:
            cities[i].append(cnt)
            cnt += 1
        else:
            pref = cities[i][0]
            cnt = 1
            cities[i].append(cnt)
            cnt += 1
    cities.sort(key=lambda x: x[2])
    for i in range(M):
        print('{:06}{:06}'.format(cities[i][0], cities[i][3]))

if __name__ == '__main__':
    main()