def main():
    N,M = map(int,input().split())
    #print(N,M)
    X = []
    for i in range(M):
        X.append(list(map(int,input().split())))
    #print(X)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                flag = 0
                for k in range(M):
                    if i+1 in X[k] and j+1 in X[k]:
                        flag = 1
                        break
                if flag == 0:
                    print('No')
                    return
    print('Yes')
    return

if __name__ == '__main__':
    main()