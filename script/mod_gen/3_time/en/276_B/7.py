def main():
    n,m = map(int,input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int,input().split())))
    roads.sort(key=lambda x: x[0])
    city = [0] * n
    for i in range(m):
        city[roads[i][0]-1] += 1
    for i in range(m):
        city[roads[i][1]-1] += 1
    for i in range(n):
        print(city[i])

if __name__ == '__main__':
    main()