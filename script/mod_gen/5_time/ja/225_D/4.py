def main():
    N, Q = map(int, input().split())
    train = [i for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1], train[query[2]-1] = train[query[2]-1], train[query[1]-1]
        elif query[0] == 2:
            for j in range(N):
                if train[j] == query[1]-1:
                    train[j] = query[2]-1
        else:
            ans = []
            for j in range(N):
                if train[j] == train[query[1]-1]:
                    ans.append(j+1)
            print(len(ans), *ans)

if __name__ == '__main__':
    main()