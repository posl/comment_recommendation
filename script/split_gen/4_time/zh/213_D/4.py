def main():
    n = int(input())
    roads = []
    for i in range(n-1):
        roads.append(list(map(int, input().split())))
    cities = [1]
    for i in range(n-1):
        if roads[i][0] == cities[-1]:
            cities.append(roads[i][1])
        elif roads[i][1] == cities[-1]:
            cities.append(roads[i][0])
    print(*cities)
