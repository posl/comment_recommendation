def main():
    N, Q = map(int, input().split())
    train = [i for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1], train[query[2]-1] = train[query[2]-1], train[query[1]-1]
        elif query[0] == 2:
            train[query[1]-1], train[query[2]-1] = train[query[2]-1], train[query[1]-1]
        else:
            target = train[query[1]-1]
            for i in range(N):
                if target == train[i]:
                    print(i+1, end=' ')
            print()
