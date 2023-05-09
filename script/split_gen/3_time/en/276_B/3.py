def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort()
    cities = []
    for i in range(n):
        cities.append([])
    for i in range(m):
        cities[roads[i][0] - 1].append(roads[i][1])
    for i in range(n):
        print(len(cities[i]), end = ' ')
        for j in range(len(cities[i])):
            print(cities[i][j], end = ' ')
        print()
