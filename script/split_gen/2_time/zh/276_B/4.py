def main():
    n,m = map(int, input().split())
    roads = []
    for i in range(m):
        a,b = map(int, input().split())
        roads.append((a,b))
    roads.sort()
    for i in range(1,n+1):
        print(len([road[1] for road in roads if road[0] == i]), end=' ')
        for road in roads:
            if road[0] == i:
                print(road[1], end=' ')
        print()
