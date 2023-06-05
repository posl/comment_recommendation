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
            if train[j][0] >= query[i][0] and train[j][1] <= query[i][1]:
                count += 1
        print(count)
main()
