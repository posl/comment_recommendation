def main():
    N, Q = map(int, input().split())
    ans = []
    train = [[] for _ in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1] - 1, query[2] - 1
            train[x].append(y)
            train[y].append(x)
        elif query[0] == 2:
            x, y = query[1] - 1, query[2] - 1
            train[x].remove(y)
            train[y].remove(x)
        elif query[0] == 3:
            x = query[1] - 1
            ans.append(train[x])
    for i in range(len(ans)):
        print(len(ans[i]), *ans[i])

if __name__ == '__main__':
    main()