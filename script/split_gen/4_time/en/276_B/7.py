def main():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, sys.stdin.readline().split())))
    roads.sort()
    cities = [[] for i in range(n)]
    for i in roads:
        cities[i[0]-1].append(i[1])
    for i in range(n):
        print(len(cities[i]), end=' ')
        for j in cities[i]:
            print(j, end=' ')
        print()
