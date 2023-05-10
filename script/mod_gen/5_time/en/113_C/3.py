def main():
    n, m = map(int, input().split())
    city = []
    for i in range(m):
        p, y = map(int, input().split())
        city.append([i, p, y])
    city.sort(key=lambda x: x[2])
    city.sort(key=lambda x: x[1])
    #print(city)
    for i in range(m):
        city[i].append(str(city[i][1]).zfill(6) + str(i+1).zfill(6))
    city.sort(key=lambda x: x[0])
    for i in range(m):
        print(city[i][3])

if __name__ == '__main__':
    main()