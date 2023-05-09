def main():
    n, m, q = map(int, input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        count = 0
        for train in trains:
            if query[0] <= train[0] and train[1] <= query[1]:
                count += 1
        print(count)
