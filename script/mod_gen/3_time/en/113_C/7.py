def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]
    # sort by Y_i
    cities.sort(key=lambda x: x[1])
    # sort by P_i
    cities.sort(key=lambda x: x[0])
    #print(cities)
    # count cities for each prefecture
    count = [0] * (N + 1)
    for city in cities:
        count[city[0]] += 1
    #print(count)
    # make ID numbers
    for city in cities:
        print("{:06}{:06}".format(city[0], count[city[0]]))
        count[city[0]] -= 1

if __name__ == '__main__':
    main()