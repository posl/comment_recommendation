def main():
    N, Q = map(int, input().split())
    train = [ i for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]] = train[query[2]]
        elif query[0] == 2:
            train[query[1]] = query[1]
            train[query[2]] = query[2]
        else:
            print(' '.join(map(str, [i for i, x in enumerate(train) if x == train[query[1]]])))
