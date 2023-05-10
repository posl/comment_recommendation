def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    if N>=M:
        print(0)
        exit()
    X_dif = []
    for i in range(M-1):
        X_dif.append(X[i+1]-X[i])
    X_dif.sort()
    print(sum(X_dif[:M-N]))

if __name__ == '__main__':
    main()