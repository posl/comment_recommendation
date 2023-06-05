def main():
    n, q = map(int, input().split())
    roads = []
    for i in range(n-1):
        roads.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] > query[1]:
            query[0], query[1] = query[1], query[0]
        for road in roads:
            if road[0] > road[1]:
                road[0], road[1] = road[1], road[0]
        if query[0] == query[1]:
            print('Town')
        else:
            for road in roads:
                if query[0] == road[0] and query[1] == road[1]:
                    print('Road')
                    break
                elif query[0] == road[0] and query[1] == road[1]:
                    print('Road')
                    break
                elif query[0] > road[0] and query[1] < road[1]:
                    print('Town')
                    break
                elif query[0] < road[0] and query[1] > road[1]:
                    print('Town')
                    break
            else:
                print('Road')
