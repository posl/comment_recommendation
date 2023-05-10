def main():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))
    roads.sort()
    cities = [0] * N
    for i in range(M):
        cities[roads[i][0] - 1] += 1
        cities[roads[i][1] - 1] += 1
    for i in range(N):
        print(cities[i])
