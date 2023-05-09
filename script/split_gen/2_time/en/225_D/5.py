def main():
    N, Q = map(int, input().split())
    trains = [i for i in range(N+1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            trains[query[1]], trains[query[2]] = trains[query[2]], trains[query[1]]
        elif query[0] == 2:
            trains[query[1]], trains[query[2]] = trains[query[2]], trains[query[1]]
        elif query[0] == 3:
            train = query[1]
            while trains[train] != train:
                print(train, end=' ')
                train = trains[train]
            print(train, end=' ')
            print()
    return
