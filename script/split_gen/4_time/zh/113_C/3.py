def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        p, y = map(int, input().split())
        cities.append((i, p, y))
    cities.sort(key=lambda x: x[2])
    cities.sort(key=lambda x: x[1])
    ids = [0] * M
    for i in range(M):
        ids[cities[i][0]] = str(cities[i][1]).zfill(6) + str(i + 1).zfill(6)
    for i in range(M):
        print(ids[i])
