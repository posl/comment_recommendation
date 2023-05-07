def main():
    N, Q = map(int, input().split())
    train = [[i+1, i+1, 1] for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            y = query[2]
            if train[x-1][1] == y:
                continue
            if train[x-1][0] != x:
                train[train[x-1][0]-1][1] = train[y-1][1]
                train[train[y-1][1]-1][0] = train[x-1][0]
                train[train[x-1][0]-1][2] += train[y-1][2]
            else:
                train[x-1][1] = train[y-1][1]
                train[y-1][0] = x
                train[x-1][2] += train[y-1][2]
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            if train[x-1][1] != y:
                continue
            if train[x-1][0] != x:
                train[train[x-1][0]-1][1] = y
                train[y-1][0] = train[x-1][0]
                train[train[x-1][0]-1][2] += train[y-1][2]
            else:
                train[x-1][1] = y
                train[y-1][0] = x
                train[x-1][2] -= train[y-1][2]
        else:
            x = query[1]
            print(train[x-1][2], end=" ")
            while train[x-1][0] != x:
                x = train[x-1][0]
                print(x, end=" ")
            print()

if __name__ == '__main__':
    main()