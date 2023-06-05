def solve():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort(key=lambda x: x[1])
    roads.sort(key=lambda x: x[0])
    for i in range(1, n+1):
        print(len([x for x in roads if x[0] == i]) + len([x for x in roads if x[1] == i]), end=' ')
        for x in roads:
            if x[0] == i:
                print(x[1], end=' ')
            elif x[1] == i:
                print(x[0], end=' ')
        print()
