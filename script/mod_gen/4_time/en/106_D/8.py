def main():
    n,m,q = map(int,input().split())
    train = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        l,r = map(int,input().split())
        train[i][l-1] += 1
        if r < n:
            train[i][r] -= 1
    for i in range(m):
        for j in range(n-1):
            train[i][j+1] += train[i][j]
    for i in range(m):
        for j in range(n-1):
            train[i][j+1] += train[i][j]
    for i in range(q):
        p,q = map(int,input().split())
        print(train[i][q-1]-train[i][p-2])

if __name__ == '__main__':
    main()