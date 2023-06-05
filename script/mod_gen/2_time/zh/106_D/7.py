def main():
    n,m,q = map(int,input().split())
    train = []
    for i in range(m):
        train.append(list(map(int,input().split())))
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        count = 0
        for j in range(m):
            if query[i][0] <= train[j][0] and query[i][1] >= train[j][1]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()