def main():
    N, Q = map(int, input().split())
    trains = [[] for _ in range(N)]
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1]) - 1
            y = int(query[2]) - 1
            trains[x].append(y)
            trains[y].append(x)
        elif query[0] == "2":
            x = int(query[1]) - 1
            y = int(query[2]) - 1
            trains[x].remove(y)
            trains[y].remove(x)
        else:
            x = int(query[1]) - 1
            print(*[a + 1 for a in trains[x]])
