def main():
    N, M = map(int, input().split())
    cities = []
    prefectures = [0] * N
    for i in range(M):
        P, Y = map(int, input().split())
        cities.append([P, Y, i])
        prefectures[P - 1] += 1
    cities.sort(key=lambda x: x[1])
    ids = [0] * M
    for i in range(M):
        ids[cities[i][2]] = str(cities[i][0]).zfill(6) + str(prefectures[cities[i][0] - 1]).zfill(6)
        prefectures[cities[i][0] - 1] -= 1
    for i in range(M):
        print(ids[i])
