def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))
    roads.sort()
    cities = [0 for _ in range(n)]
    for a, b in roads:
        cities[a-1] += 1
        cities[b-1] += 1
    for i in range(n):
        print(cities[i])

if __name__ == '__main__':
    main()