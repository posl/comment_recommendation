def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(N):
        for j in range(N):
            if i != j and not any([i+1 in x[k] and j+1 in x[k] for k in range(M)]):
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()