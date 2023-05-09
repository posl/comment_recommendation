def main():
    N, Q = map(int, input().split())
    train = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        train[i][0] = i - 1
        train[i][1] = i + 1
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[train[query[1]][0]][1] = train[query[1]][1]
            train[train[query[1]][1]][0] = train[query[1]][0]
            train[query[1]][0] = train[query[2]][0]
            train[query[1]][1] = query[2]
            train[train[query[2]][0]][1] = query[1]
            train[query[2]][0] = query[1]
        elif query[0] == 2:
            train[train[query[1]][0]][1] = train[query[2]][0]
            train[train[query[2]][0]][0] = train[query[1]][0]
            train[train[query[2]][1]][0] = query[1]
            train[query[2]][0] = query[1]
            train[query[1]][0] = train[query[2]][1]
            train[query[1]][1] = query[2]
        else:
            ans = []
            now = query[1]
            while now != 0:
                ans.append(now)
                now = train[now][1]
            print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()