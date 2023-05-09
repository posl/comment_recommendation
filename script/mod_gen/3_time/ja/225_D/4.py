def main():
    n,q = map(int,input().split())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    #print(query)
    train = [i for i in range(n+1)]
    #print(train)
    for i in range(q):
        if query[i][0] == 1:
            train[query[i][1]] = query[i][2]
        elif query[i][0] == 2:
            train[query[i][1]] = query[i][1]
        else:
            print(train[query[i][1]])

if __name__ == '__main__':
    main()