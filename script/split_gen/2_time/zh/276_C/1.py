def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for i in range(m)]
    cities = [[] for i in range(n)]
    for a, b in roads:
        cities[a-1].append(b)
        cities[b-1].append(a)
    for i in range(n):
        print(len(cities[i]), end=" ")
        print(*sorted(cities[i]))
